#include<bits/stdc++.h>
using namespace std;
#define err(x) cout<<#x<<"= "<<x<<endl;
#define FOR(i,a,b) for(int i =a; i< b; ++i)
#define rep(i,n) FOR(i,0,n)
#define pb push_back
#define INF 1000000000
#define TRVI(it,it1,it2) for(vi::iterator it = it1; it!= it2; it++)
#define ff first
#define ss second
#define mp make_pair
#define pq priority_queue<int, vector<int>, greater<int> >
#define ll long long
const ll PR = 1000000009;
#define SIZE (24*60)
#define vi vector<int>
#define pii pair<int,int>
#define endl '\n'

int sta[24*60],end[24*60];

int cmp(int a, int b){
	return a>b;
}
int main(){
//	#ifdef ONLINE_JUDGE
//	freopen("a.in", "r" , stdin);
//	freopen("a.out", "w", stdout);
//      cin.tie(false); cout.tie(false);	
//	#endif
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	rep(t1, t){
		rep(i,SIZE)sta[i] = end[i] = 0;
		int ans=0,ac,an,to1=720,to2=720;
		cin>>ac>>an;
		rep(i,ac){
			int a,b;
			cin>>a>>b;//a--;b--;
			if(a==b)continue;
			to1-= b-a;
			sta[a] = 1;
			end[b-1] = 1;
		}
		rep(i, an){
			int a,b;
			cin>>a>>b;//a--;b--;
			if(a==b)continue;
			to2-= b-a;
			sta[a] =-1;
			end[b-1] = -1;
		}
		vector<int> pp,mm;
		int storst=0,storsti,prevst=0,prevind;
		rep(i, SIZE){
			if(sta[i] != 0){
				int st = sta[i],stid=i;
				if(storst==0){storst=st;storsti=i;}
				while(end[i]==0)i++;
				
				if(prevst!=0){
					if(prevst==1 && st==1){
						pp.pb(stid-prevind);
						to1-= stid-prevind;
					}
					else
					if(prevst==-1 && st==-1){
						mm.pb(stid-prevind);
						to2-= stid-prevind;
					}
					else ans++;
				}
				prevst=st;
				prevind = i+1;;
			}
		}
//		cout<<storst<<' '<<prevind<<endl;
		if(prevst==1 && storst==1){
			pp.pb(storsti+ 60*24 - prevind);
			to1-= pp.back();
		}
		else if(prevst==-1 && storst==-1){
			mm.pb(storsti+ 60*24 - prevind);
			to2-= mm.back();
		}
		else ans++;
		sort(pp.begin(), pp.end());
		sort(mm.begin(), mm.end());
		while(to1<0){
			ans+=2;
			if(pp.back() > -1*to1){
				to1=0;
			}
			else to1+= pp.back();
			pp.pop_back();
		}

		while(to2<0){
			ans+=2;
			if(mm.back() > -1*to2){
				to2=0;
			}
			else to2+= mm.back();
			mm.pop_back();
		}
		cout<<"Case #"<<t1+1<<": ";
		cout<<ans<<endl;
	}
			



	return 0;
};
