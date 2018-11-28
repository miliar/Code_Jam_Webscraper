// AUTHOR VINAYAK SINGLA
#include<bits/stdc++.h>
using namespace std;
#define ff first 
#define ss second 

bool sortway(pair<int,int> a,pair<int,int> b){
    if(a.ss=b.ss){
        return b.ff<a.ff;
    }
    return b.ss<a.ss;
}

string s[25];
int igr[50];
int qt[50][50];
int main()
{
    std::ios::sync_with_stdio(false);
    int a,q,b,c,n,r,p,ans;
    double f,ff;
    cin>>q;
    for(int k=0;k<q;k++){
        ans=0;
        vector<pair<int,int> >pq[50];
        cin>>n>>p;
        for(int i=0;i<n;i++)cin>>igr[i];
        for(int i=0;i<n;i++){
            for(int j=0;j<p;j++){
                cin>>qt[i][j];
                f=((qt[i][j]+0.0)/igr[i]);
                ff=((qt[i][j])/igr[i]);
                if(f-ff>.5)a=ceil(f);
                else a=floor(f);
                if(a!=0 &&  (abs(a*igr[i]-qt[i][j])+0.0)/(a*igr[i])<=.1 )
                    pq[i].push_back({ceil((10*qt[i][j]+0.0)/(11*igr[i])),floor((10*qt[i][j]+0.0)/(9*igr[i]))});
            }
        }
        for(int i=0;i<n;i++)sort(pq[i].begin(),pq[i].end(),sortway);
        int left=0,right=0;
        if(n==2){
            for(int i=0;(i<p && left<pq[0].size() && right<pq[1].size() ) ;i++){
                    if(pq[0][left].ff>pq[1][right].ss){
                        left++;
                    }
                    else if(pq[0][left].ss<pq[1][right].ff){
                        right++;
                    }
                    else{
                        ans++;
                        left++;
                        right++;
                    }
                }
                cout<<"Case #"<<k+1<<": "<<ans<<endl;
            }
        else{
            cout<<"Case #"<<k+1<<": "<<pq[0].size()<<endl;
        }
        
	}
    return 0;
}
