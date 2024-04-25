"""Synthetic join audit; contains no original health or green-space records."""
import json

def audit(left_ids, right_ids):
    left=list(left_ids);right=list(right_ids)
    left_set=set(left);right_set=set(right)
    return {
        'left_rows':len(left), 'right_rows':len(right),
        'duplicate_left':sorted({x for x in left if left.count(x)>1}),
        'duplicate_right':sorted({x for x in right if right.count(x)>1}),
        'unmatched_left':sorted(left_set-right_set),
        'unmatched_right':sorted(right_set-left_set),
        'one_to_one':len(left)==len(left_set) and len(right)==len(right_set) and left_set==right_set,
        'original_join_reproduced':False,
    }

if __name__=='__main__':
    print(json.dumps(audit(['A','B','C'],['A','B','B','D']),indent=2))
