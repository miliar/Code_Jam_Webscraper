#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>
#define PI 3.1415926535897932384626433832795028L
using namespace std;
int T;
pair<int, int> p[1001];
long long s[1001];
priority_queue<long long, vector<long long>, greater<long long> > q;
bool cmp(pair<int, int> a, pair<int, int> b)
{
    return a.first<b.first; 
}
int main() {
    scanf("%d", &T);
    for (int c=0; c<T; c++)
    {
        printf("Case #%d: ", c+1);
        int n, k;
        scanf("%d%d", &n, &k);
        for (int i=0; i<n; i++)
        {
            int r, h;
            scanf("%d%d", &r, &h);
            p[i]=pair<int, int>(r, h);
        }
        sort(p, p+n, cmp);
        for (int i=0; i<n; i++)
        {
            s[i]=(long long)p[i].first*p[i].second*2LL;
        }
        long long ans=0;
        long long sum=0;
        q=priority_queue<long long, vector<long long>, greater<long long> >();
        for (int i=0; i<k-1; i++)
        {
            q.push(s[i]);
            sum+=s[i];
        }
        ans=max(ans, sum+(long long)p[k-1].first*p[k-1].first+s[k-1]);
        for (int i=k; i<n; i++)
        {
            if (1!=k && s[i-1]>q.top())
            {
                sum+=s[i-1]-q.top();
                q.pop();
                q.push(s[i-1]);
                //printf("%d %lld\n", i, s[i-1]);
                
            }
            //printf("sum %lld\n", sum);
            ans=max(ans, sum+(long long)p[i].first*p[i].first+s[i]);
        }
        //printf("%lld\n", ans);
        printf("%.10Lf\n", (long double)PI*ans);
    }
	// your code goes here
	return 0;
}
