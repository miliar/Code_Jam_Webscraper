#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl '\n'
typedef long long ll;
using namespace std;

int N,P;

int findElem(vector<int>&groups,int s){
	for (int i = 0; i < N; ++i)
	{
		if (groups[i]%P==s){
			return i;
		}
	}
	return -1;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin>>T;
	for (int tc=0; tc<T; tc++){
		cin>>N>>P;
		vector<int>groups(N);
		for (int i = 0; i < N; ++i)
		{
			cin>>groups[i];
		}
		int ans=0;
		if (P!=4){
			int cur=0;
			for (int i = 0; i < N; ++i)
			{
				int search=(P-cur)%P;
				int ind=-1;
				for (int j = 0; j < P; ++j)
				{
					ind=findElem(groups,(search+j)%P);
					if (ind>=0){
						break;
					}
				}
				if (cur==0)
					ans++;
				cur=(cur+groups[ind])%P;
				groups[ind]=-1;
			}
		} else{
			vector<int> occur(4);
			for (int i = 0; i < N; ++i)
			{
				occur[groups[i]%4]++;
			}
			ans+=occur[0];
			ans+=(occur[2]/2);
			occur[2]-=(occur[2]/2)*2;
			int temp=min(occur[1],occur[3]);
			ans+=temp;
			occur[1]-=temp;
			occur[3]-=temp;
			temp=min(occur[2],occur[1]/2);
			ans+=temp;
			occur[2]-=temp;
			occur[1]-=2*temp;
			temp=occur[1]/4;
			ans+=temp;
			occur[1]-=temp*4;
			temp=min(occur[2],occur[3]/2);
			ans+=temp;
			occur[2]-=temp;
			occur[3]-=temp*2;
			int cur=0;
			while(true){
				if (occur[1]>0){
					occur[1]--;
					if (cur==0)
						ans++;
					cur=(cur+1)%4;
				} else if (occur[2]>0){
					occur[2]--;
					if (cur==0)
						ans++;
					cur=(cur+2)%4;
				} else if (occur[3]>0){
					occur[3]--;
					if (cur==0)
						ans++;
					cur=(cur+3)%4;
				} else{
					break;
				}
			}
		}
		cout<<"Case #"<<tc+1<<": "<<ans<<endl;
	}
}