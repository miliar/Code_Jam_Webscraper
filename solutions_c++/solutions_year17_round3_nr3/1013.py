#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
typedef long long ll;
typedef pair<int,int> PII;
#define REP(i,n) for(int (i)=0;(i)<n;(i)++)

int main() {cout.sync_with_stdio(false);cin.tie(0);cout.tie(0);cerr.tie(0);
int _case;cin >> _case;
for(int casen=1;casen<=_case;casen++){
int N,K;cin >> N>>K;
double U;cin >> U;
double P[N];
for(int i=0;i<N;i++)cin >> P[i];

sort(P,P+N);
double ans=0;


double A[K];
for(int i=0;i<K;i++)A[i]=P[i+N-K];


double sum[K];
memset(sum,0,sizeof sum);
sum[0]=A[0];
for(int i=1;i<K;i++)sum[i]=sum[i-1]+A[i];
if(sum[K-1]+U>=K)ans=1;
else{
  for(int i=0;i<K;i++){
    double avg=(sum[i]+U)/(i+1);
    //cerr<<"Here"<<avg<<endl;
    if(i==K-1 || avg<=A[i+1]){
      //cerr<<"asd"<<endl;
      for(int j=0;j<=i;j++){
        A[j]=avg;
      }
      break;
    }
  }
}

for(int i=0;i<K;i++)P[i+N-K]=A[i];

//if(casen==95){cout << N<<endl;for(int i=0;i<N;i++)cerr << P[i]<<" ";cerr << endl;}

if(ans<1){
ans=0;
//calculate with current upgrades
map<int,double> trials,trials2;
trials[0]=1;
for(int i=0;i<N;i++){
  trials2.clear();
  for(auto j:trials){
    trials2[j.X+1]+=j.Y*P[i];
    trials2[j.X]+=j.Y*(1-P[i]);
  }
  swap(trials,trials2);
}
//for(auto i:trials)cerr << i.X<<" "<<i.Y<<endl;
for(auto i:trials)if(i.X<K)ans+=i.Y;
ans=1-ans;
}
cout << "Case #"<<casen<<": ";
cout <<setprecision(15)<<fixed<<ans;
cout << endl;
}
}
