#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);

    //ios::sync_with_stdio(false);
    int tc;
    scanf("%d", &tc);
    for(int case_no=1; case_no<=tc; case_no++)
    {
        printf("Case #%d:", case_no);
        cerr << "Geval " << case_no << " gestart" << endl;
        int N, P;
        scanf("%d %d", &N, &P);
        vector<int> needed(N);
        for(int i=0; i<N; i++) scanf("%d", &needed[i]);

        int MAX_AVAILABLE=-1;
        vector< vector<int> > packages(N, vector<int>(P));
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<P; j++)
            {
                scanf("%d", &packages[i][j]);
                MAX_AVAILABLE=max(packages[i][j], MAX_AVAILABLE);
            }
        }

        vector< vector< pair<int, int> > > pairs(N);
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<P; j++)
            {
                int hoogstens = (10*packages[i][j])/(9*needed[i]);
                int minstens = (10*packages[i][j]+(11*needed[i])-1)/(11*needed[i]);
                if(minstens<=hoogstens && minstens>0) pairs[i].push_back(make_pair(minstens, hoogstens)); // maybe change "minstens>0" constraint.
            }
            sort(pairs[i].begin(), pairs[i].end());
        }

        vector<int> last_index(N, -1);
        int nb_matches=0;
        int used=1;
        int MAX_GRENS=min(MAX_AVAILABLE*2, 1300000);
        while(used <= MAX_GRENS)
        {
            bool found=false;
            vector<int> current_indices(N);

            bool broken=false;
            for(int i=0; i<N; i++)
            {
                int max_mogelijke_index = pairs[i].size();
                max_mogelijke_index--;
                if(last_index[i]+1>max_mogelijke_index)
                {
                    broken=true;
                    break;
                }
                int lo = last_index[i]+1;
                int hi = max_mogelijke_index;
                while(lo<hi)
                {
                    int mid = (lo+hi)/2;
                    if(pairs[i][mid].second >=  used)
                    {
                        hi=mid;
                    }
                    else
                    {
                        lo=mid+1;
                    }
                }
                if(pairs[i][lo].first <= used && used <= pairs[i][lo].second)
                {
                    current_indices[i]=lo;
                }
                else
                {
                    broken=true;
                    break;
                }
            }
            if(!broken)
            {
                found=true;
                nb_matches++;
                for(int i=0; i<N; i++)
                {
                    last_index[i]=current_indices[i];
                }
            }

            if(!found)
            {
                used++;
            }
        }
        printf(" %d\n", nb_matches);
    }
    return 0;
}
