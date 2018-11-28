#include <bits/stdc++.h>
using namespace std;

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cs; cin>>cs;
    for(int t=1; t<=cs; t++) {
        set<pair<int, pair<int, int> > > s;
        int n, k;
        cin>>n>>k;
        printf("Case #%d: ", t);
        s.insert({-n, {0, n+1}});
        for(int i=1; i<k; i++) {
            auto top=*(s.begin());
            s.erase(s.begin());
            int left=top.second.first;
            int right=top.second.second;
            int mid=(left+right)/2;
            s.insert({-(mid-left-1), {left, mid}});
            s.insert({-(right-mid-1), {mid, right}});
        }
        auto top=*(s.begin());
        int left=top.second.first;
        int right=top.second.second;
        int mid=(left+right)/2;
        int l=mid-left-1;
        int r=right-mid-1;
        printf("%d %d\n", max(l, r), min(l, r));
    }
    return 0;
}
/*
100
4 2
5 2
6 2
1000 1000
1000 1
1000 512
259 226
988 953
999 277
661 587
1000 464
277 236
1000 511
999 497
1000 128
3 1
479 376
999 488
999 255
2 1
1000 2
757 627
528 406
941 913
3 2
399 303
1000 127
500 244
555 456
999 499
451 410
860 769
500 2
479 451
481 394
750 630
299 238
898 832
999 999
999 512
545 476
999 998
5 1
601 453
1000 489
999 500
500 248
299 276
1000 256
1000 503
675 594
500 127
459 365
500 205
500 246
2 2
339 258
500 500
999 127
999 1
500 101
999 487
999 511
410 405
999 498
843 837
1 1
1000 999
4 1
1000 498
629 617
1000 500
1000 499
806 713
937 854
500 245
500 249
374 355
500 255
868 695
974 899
598 569
595 452
454 367
500 116
458 351
612 605
500 499
999 2
693 539
500 256
1000 255
999 128
1000 488
767 730
500 1
500 128
999 256
500 250
500 117
*/
