from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from ..models import Diary


class LoggedInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""

        # テストユーザーのパスワード
        self.password = ''
