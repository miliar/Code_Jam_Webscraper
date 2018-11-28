#include<bits/stdc++.h>
using namespace std;
int N, P;
int arr[99][99];
pair<int, int> interval[99][99];
int R[99];
pair<int, int> getInterval(int a, int b)
{
    // 10a/11b <= t <= 10a / 9b
    //equiv minv <= t < maxv
    int minv = (10*a+11*b-1)/(11*b);
    int maxv = (10*a)/(9*b)+1;
    return make_pair(minv, maxv);
}
int tmain()
{
    scanf("%d%d", &N, &P);
    for(int i=0; i<N; ++i) scanf("%d", R+i);
    vector<int> eventP;
    for(int i=0; i<N; ++i)
    {
        for(int j=0; j<P; ++j)
        {
            scanf("%d",&arr[i][j]);
            interval[i][j] = getInterval(arr[i][j], R[i]);
            eventP.push_back(interval[i][j].first);
            eventP.push_back(interval[i][j].second);
        }
        sort(interval[i], interval[i]+P);
    }
    sort(eventP.begin(), eventP.end());
    eventP.resize(unique(eventP.begin(), eventP.end())-eventP.begin());
    int ans = 0;
    for(int t=0; t<eventP.size(); t++)
    {
        vector<int> ind;
        bool flag = true;
        for(int i=0; i<N; ++i)
        {
            for(int j=0; j<P; ++j)
            {
                int st = interval[i][j].first;
                int ed = interval[i][j].second;
                if(st <= eventP[t] && eventP[t] < ed)
                {
                    ind.push_back(j);
                    break;
                }
            }
            if(ind.size()==i)
            {
                flag = false;
                break;
            }
        }
        if(!flag) continue;
        t--;
        ans++;
        for(int i=0; i<N; ++i)
            interval[i][ind[i]] = make_pair(-1, -1);
    }
    return ans;
}
int main()
{
    int T;
    scanf("%d", &T);
    for(int i=1; i<=T; ++i)
        printf("Case #%d: %d\n",i,tmain());
}