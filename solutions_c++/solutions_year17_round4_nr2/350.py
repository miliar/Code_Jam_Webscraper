#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
int test;
int n, c, m;
int prom;
vector<pair<int, int> > w; //szek, ember
int elof[1009];
int helyek[1009];
bool LEHET(int kor)
{
    prom=0;
    for(int u=0; u<=n; u++) helyek[u]=0;
    int ures=1;
    for(int i=0; i<w.size(); i++)
    {
        if(helyek[w[i].F]<kor)
        {
            helyek[w[i].F]++;
            if(helyek[w[i].F]==kor && ures==w[i].F)
            {
                while(helyek[ures]==kor) ures++;
            }
        }
        else
        {
            if(ures<w[i].F)
            {
                prom++;
                helyek[ures]++;
                while(helyek[ures]==kor) ures++;
            }
            else
            {
                return false;
            }
        }
    }
    return true;
}
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        cin>>n>>c>>m;
        w.clear();
        for(int i=0; i<=1000; i++) elof[i]=0;
        for(int i=1; i<=m; i++)
        {
            int A, B;
            cin>>A>>B;
            elof[B]++;
            w.push_back({A, B});
        }
        sort(w.begin(), w.end());
        int elso=0;
        for(int i=1; i<=c; i++) elso=max(elso, elof[i]);
        int utolso=m;
        while(elso<=utolso)
        {
            int kozepso=(elso+utolso)/2;
            if(LEHET(kozepso))
            {
                utolso--;
            }
            else elso++;
        }
        LEHET(elso);
        cout<<"Case #"<<tt<<": "<<elso<<" "<<prom<<endl;
    }
    return 0;
}
