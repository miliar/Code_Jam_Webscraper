#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<int, char> ic;

int T, N, q[1010];
//  0, 1, 2, 3, 4, 5
// {R, O, Y, G, B, V}
int main(){
	scanf("%d", &T);
	for(int cas=1; cas<=T; cas++){
		scanf("%d", &N);
		printf("Case #%d: ", cas);
		for(int i=0; i<6; i++){
			scanf("%d", &q[i]);
		}
		int dif1 = q[0]-q[3], dif2 = q[4]-q[1], dif3 = q[2]-q[5];
		int min1 = min(q[0], q[3]), min2 = min(q[4], q[1]), min3 = min(q[2], q[5]); 
		//printf("*%d %d %d\n", dif1, dif2, dif3);
		if(dif1<0 || dif2<0 || dif3<0){
			printf("IMPOSSIBLE\n");
			continue;
		}
		if(dif1==0 && q[0]>0 && N>q[0]+q[3]){
			printf("IMPOSSIBLE\n");
			continue;
		}
		if(dif2==0 && q[1]>0 && N>q[1]+q[4]){
			printf("IMPOSSIBLE\n");
			continue;
		}
		if(dif3==0 && q[2]>0 && N>q[2]+q[5]){
			printf("IMPOSSIBLE\n");
			continue;
		}
		//printf("*\n");
		vector<ic> v;
		v.push_back(ic(dif1, 'R'));
		v.push_back(ic(dif3, 'Y'));
		v.push_back(ic(dif2, 'B'));
		sort(v.begin(), v.end());
		
		if(v[2].first>v[1].first+v[0].first){
			printf("IMPOSSIBLE\n");
			
			continue;
		}
		int qnt[3][1010];
		memset(qnt, 0, sizeof(qnt));
		for(int i=0; i<v[0].first; i++){
			qnt[0][i%v[2].first]++;
		}
		for(int i=v[0].first; i<v[0].first+v[1].first; i++){
			qnt[1][i%v[2].first]++;
		}
		string ans = "";
		for(int i=0; i<v[2].first; i++){
			ans += v[2].second;	
			for(int j=0; j<qnt[0][i]; j++){
				ans += v[0].second;
			}
			for(int j=0; j<qnt[1][i]; j++){
				ans += v[1].second;
			}
		}
		//cout << ans<<endl;
		int sz = ans.size();
		int i=0;
		for(i=0; i<sz; i++){
			if(ans[i]=='R') break;
		}
		string parc1="";
		for(int i=0; i<min1; i++){
			parc1 += 'R';
			parc1 += 'G';
		}	
		ans = ans.substr(0, i) + parc1 + ans.substr(i);
		
		sz = ans.size();
		i=0;
		for(i=0; i<sz; i++){
			if(ans[i]=='B') break;
		}
		string parc2="";
		for(int i=0; i<min2; i++){
			parc2 += 'B';
			parc2 += 'O';
		}	
		ans = ans.substr(0, i) + parc2 + ans.substr(i);
		
		sz = ans.size();
		i=0;
		for(i=0; i<sz; i++){
			if(ans[i]=='Y') break;
		}
		string parc3="";
		for(int i=0; i<min3; i++){
			parc3 += 'Y';
			parc3 += 'V';
		}	
		ans = ans.substr(0, i) + parc3 + ans.substr(i);
			
		cout << ans<<endl;
	}
	return 0;
}
