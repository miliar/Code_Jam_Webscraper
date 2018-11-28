// SH-RaOne //

#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ull unsigned long long int
#define ld long double
#define vi vector<int> 
#define ii pair<int,int>
#define vii vector<ii>
#define loop(x,i,a,b) for(x i=a;i<=b;i++)
#define loopi(i,a,b) for(int i=a;i<=b;i++)
#define loop2(i,a,b) for(i=a;i<=b;i++)  
#define rloop(x,i,a,b) for(x i=a;i>=b;i--)
#define rloopi(i,a,b) for(int i=a;i>=b;i--)
#define rloop2(i,a,b) for(i=a;i>=b;i--)  
#define X first
#define Y second 
//#define fill(a,x) memset(a,x,sizeof(a))
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
const long double PI = atan(1.0)*4.0;

const ll MOD = 1e9+7;
const ll INF = 1e9;
#define N 10

int AC,AJ,S1[N],S2[N],E1[N],E2[N];

void solve(){
	sort(S1,S1+AC);
	sort(S2,S2+AJ);
	sort(E2,E2+AJ);
	sort(E1,E1+AC);
	if(AC==2){
		if(E1[1]-S1[0]<=720)
			cout<<2<<endl;
		else if(E1[0] + 1440-S1[1]<=720)
			cout<<2<<endl;
		else
			cout<<4<<endl;
	}
	else if(AJ==2){
		if(E2[1]-S2[0]<=720)
			cout<<2<<endl;
		else if(E2[0] + 1440-S2[1]<=720)
			cout<<2<<endl;
		else
			cout<<4<<endl;
	}
	else if(AC==1 && AJ==0){
		cout<<2<<endl;
	}
	else if(AC==0 && AJ==1){
		cout<<2<<endl;
	}
	else if(AC==1 && AJ==1){
		cout<<2<<endl;
		// if(S1[0]<S2[0]){
		// 	int gap = S1[0] + S2[0]- E1[0] + 1440 - E2[0];
		// 	if(gap>=720)
		// 		cout<<2<<endl;
		// 	else
		// 		cout<<4<<endl;
		// }
		// else{
		// 	int gap = S2[0] + S1[0]- E2[0] + 1440 - E1[0];
		// 	if(gap>=720)
		// 		cout<<2<<endl;
		// 	else
		// 		cout<<4<<endl;
		// }
	}
}

int main()
{	
	int t;
	cin>>t;
	loop(int,T,1,t){
		cout<<"Case #"<<T<<": "; 
		cin>>AC>>AJ;
		loop(int,i,0,AC-1)
			cin>>S1[i]>>E1[i];
		loop(int,i,0,AJ-1)
			cin>>S2[i]>>E2[i];
		solve();	
	}
	return 0;
}

