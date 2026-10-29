class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return "Question: " + self.question_text

    def is_get_score(self, selected_ids):
        correct_ids = set(
            self.choice_set.filter(is_correct=True)
            .values_list('id', flat=True)
        )

        selected_ids_for_question = set(
            self.choice_set.filter(id__in=selected_ids)
            .values_list('id', flat=True)
        )

        return correct_ids == selected_ids_for_question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return "Submission by " + self.enrollment.user.username
