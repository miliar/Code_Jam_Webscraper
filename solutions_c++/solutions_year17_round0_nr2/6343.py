#include<bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define rep(i,a,b) for(i=a;i<=b;i++)
#define rep2(i,a,b,c) for(i=a;i<=b;i+=c)
#define ll long long

vector<int> vec;
int N;

bool istidy(int mas){
	int satu=mas/1000;
	int dua=mas/100;dua%=10;
	int tiga=mas/10;tiga%=10;
	int empat=mas%10;
	if(satu <= dua && dua <= tiga && tiga <= empat){
		return true;
	}
	else{
		return false;
	}
}

int main(){
//	freopen("BBBin.txt","r",stdin);
//	freopen("BBBout.txt","w",stdout);
	int tes;
	int i;
	rep(i,1,1000){
		if(istidy(i)){
			vec.pb(i);
		}
	}
	cin>>tes;
	int cas=0;
	while(tes--){
		cin>>N;
		cas++;
		cout<<"Case #"<<cas<<": ";
		cout<<*(upper_bound(vec.begin(),vec.end(),N)-1)<<"\n";
	}
}

