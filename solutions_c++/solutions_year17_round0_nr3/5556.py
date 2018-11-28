#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
using namespace std;

int main()
{
    //read
    freopen("C-small-1-attempt0.in", "rt", stdin);
    freopen("C-small-1-attempt0.out", "wt", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        long long N, K;
        cin >> N >> K;

        multiset< pair<int, pair<int,int> > > myset;
        pair<int,int> pii = make_pair(1,N);
        pair<int, pair<int,int> > pipii = make_pair(N,pii);
        myset.insert(pipii);
        //initialized

        int x, y; //x<=y

        for (int i=1;i<=K;i++) { //for each person
                
                multiset< pair<int, pair<int,int> > >::iterator it1;
                it1 = myset.end();
                it1--;
                int siz = (*it1).first;
            multiset< pair<int, pair<int,int> > >::iterator it;
            it = myset.end();
            //it--; //now 'it' is at the last
                int k = siz;
                do {
                    it--;
                    k = (*it).first;
                } while ( k == siz && it != myset.begin());

                if (k != siz) it++;

            int a = (*it).second.first; //begin of biggest gap
            int b = (*it).second.second; //end of biggest gap

            myset.erase(it);
            //and now we add two gaps
            pair<int, int> pii1;
            pair<int, int> pii2;
            pair<int, pair<int, int> > pipii1;
            pair<int, pair<int, int> > pipii2;
            //there are two cases
            if (siz%2==1) {
                pii1 = make_pair(a,siz/2-1+a);
                pipii1 = make_pair(siz/2,pii1);
                pii2 = make_pair(siz/2+1+a,b);
                pipii2 = make_pair(siz/2,pii2);
            }
            else if (siz%2==0) {
                pii1 = make_pair(a,siz/2-2+a);
                pipii1 = make_pair(siz/2-1,pii1);
                pii2 = make_pair(siz/2+a,b);
                pipii2 = make_pair(siz/2,pii2);
            }
            x = pipii1.first;
            y = pipii2.first;
            myset.insert(pipii1);
            myset.insert(pipii2);

        }

        cout << "Case #" << t << ": " << y << " " << x << endl;
    }

    return 0;
}
