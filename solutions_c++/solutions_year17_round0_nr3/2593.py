#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
map<LL, LL> A;
map<LL,bool> queued;
vector <pair<LL,LL> > Y;
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("outC.txt", "w", stdout);
    int t;
    cin>>t;

    for(int cs=1; cs<=t; cs++)
    {
        LL n, k;
        cin>>n>>k;
        LL g=n;
        A[n] = 1;
        queue<LL> q;
        q.push(n);
        queued[n] = 1;
        while(!q.empty())
        {
            LL num = q.front();
            q.pop();
            LL mp;
            if(num != n)
            {
                if(A.count(num*2))     A[num] += A[num*2];
                if(A.count((num+1)*2))   A[num] += A[(num+1)*2];
                if(A.count(num*2+1))   A[num] += A[num*2+1]*2;
            }
            num--;
            mp = num/2;
            LL mp2 = num - mp;
            if(mp2 > 0 && !queued[mp2])   queued[mp2] = 1,q.push(mp2);
            if(mp > 0 && !queued[mp])     queued[mp] = 1,q.push(mp);
        }
        for(auto V:A)Y.push_back(V);
        reverse(Y.begin(),Y.end());
        for(auto V:Y)
        {
            LL R1=V.first;
            LL R2=V.second;
            if(k <= R2)
            {
                LL mp1,mp2;
                LL cc = R1;
                cc--;
                mp1 = cc/2;
                cc -= mp1;
                mp2 = cc;
                cout<<"Case #"<<cs<<": "<<max(mp2,mp1)<<' '<<min(mp1,mp2)<<endl;
                break;
            }
            k -= R2;
        }
        queued.clear();
        A.clear();
    }

    return 0;
}


