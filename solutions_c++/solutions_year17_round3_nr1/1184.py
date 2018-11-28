#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
typedef long long ll;
#define REP(i,n) for(int (i)=0;(i)<n;(i)++)

int main() {cout.sync_with_stdio(false);cin.tie(0);cout.tie(0);cerr.tie(0);
int _case;cin >> _case;
for(int casen=1;casen<=_case;casen++){

ll N,K;cin >> N>>K;
ll R[N],H[N];
pair<ll,ll> qwe[N];

for(int i=0;i<N;i++)cin >> R[i]>>H[i];
//for(int i=0;i<N;i++){qwe[i].X=-H[i];qwe[i].Y=-R[i];}
for(int i=0;i<N;i++){qwe[i].X=-H[i]*R[i]*2;qwe[i].Y=-R[i];}

sort(qwe,qwe+N);
ll maxr=-1;
ll ans=0;
ll sumsidearea=0;
for(int i=0;i<K-1;i++)maxr=max(maxr,-qwe[i].Y);
for(int i=0;i<K-1;i++)sumsidearea+=-qwe[i].X;

for(int i=K-1;i<N;i++){
  ll R=max(maxr,-qwe[i].Y);
  ll _curr=R*R+sumsidearea-qwe[i].X;

  ans=max(ans,_curr);
}

//cout << maxr<<endl;

//for(int i=K;i<N;i++)


cout << "Case #"<<casen<<": ";
cout <<setprecision(26)<< ans*M_PI;
cout << endl;
}
}
