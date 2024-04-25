import unittest
from examples.audit_join import audit

class JoinAuditTests(unittest.TestCase):
    def test_clean_join(self): self.assertTrue(audit(['A','B'],['B','A'])['one_to_one'])
    def test_duplicates(self): self.assertEqual(audit(['A'],['A','A'])['duplicate_right'],['A'])
    def test_unmatched_both_sides(self):
        r=audit(['A','B'],['B','C'])
        self.assertEqual(r['unmatched_left'],['A']);self.assertEqual(r['unmatched_right'],['C'])
    def test_empty_sets_match(self): self.assertTrue(audit([],[])['one_to_one'])
    def test_original_not_reproduced(self): self.assertFalse(audit(['A'],['A'])['original_join_reproduced'])

if __name__=='__main__': unittest.main()
