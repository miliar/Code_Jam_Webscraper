/*While alive CODE*/

                    /*War will happen and code will follow*/

#include <bits/stdc++.h>
using namespace std;
#define mem(x,y) memset(x,y,sizeof(x))
#define bitcount    __builtin_popcountll
#define mod 1000000007
#define N 1000009
#define fast ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define ss(s) cin>>s;
#define si(x)  scanf("%d",&x);
#define sl(x)  cin>>x;
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
#define S second
#define F first
#define ll long long 
ll power(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
string a,c;
int q,n,t,r,o,y,g,b,v;
int arr[N];
int brr[N];
int main()
{
  freopen("B-small-attempt3.in", "r", stdin);
    freopen("Output361.out", "w", stdout);


cin>>t;
for(int yi=0;yi<t;yi++)
        {	//cerr << yi <<  endl;
        	cin >> n;
        	cin >> r >> o >> y >> g >> b >> v;
        	string cur = "";
        	int prev = -1;
        	int rtem,ytem,btem;
        	string ans="";
        	if(r == 0 && y == 0 ){
        		if(b!=1)
        			 ans ="IMPOSSIBLE";
        		else ans ="B";
        	
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;
        	}
        	if(r == 0 && b == 0 ){
        		if(y!=1)
        			 ans ="IMPOSSIBLE";
        		else ans ="Y";
        	
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;
        	}
        	if(b == 0 && y == 0 ){
        		if(r!=1)
        			 ans ="IMPOSSIBLE";
        		else ans ="R";
        	
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;
        	}
        	rtem = r;
        	ytem = y;
        	btem  = b;

        	while(rtem>=0 || ytem>=0 || btem>=0){
        		if(rtem < 0 || ytem <0 || btem < 0)break;
        		if(!rtem && !ytem && prev == 2)break;
        			if(!btem && !ytem && prev == 0)break;
        			if(!rtem && !btem && prev == 1)break;
        			if(rtem>=ytem && rtem>=btem && prev!=0){
        				cur+='R';
        				prev = 0;
        				rtem--;
        				continue;
        			}
        			if(ytem>=rtem && ytem>=btem && prev!=1){
        				cur+='Y';
        				prev = 1;
        				ytem--;
        				continue;
        			}
        			if(btem>=rtem && btem>=ytem && prev!=2){
        				cur+='B';
        				prev = 2;
        				btem--;
        				continue;
        			}
        			if(prev == 0){
        				if(ytem>btem){
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				}}
        			if(prev == 1){
        				if(rtem>btem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				} }
        			if(prev == 2){
        				if(rtem>ytem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        			}
        			break;



        	}
        	bool pos = true;
        	ans="";
        	for(int i = 0;i<cur.size() - 1;i++){
        		if(cur[i] == cur[i+1])pos = false;
        	}
        	if(cur[0] ==  cur[cur.size() - 1])pos = false;
        	if(pos && cur.size() == n){
        		ans = cur;
        	}
        	else ans ="IMPOSSIBLE";
        	if(ans != "IMPOSSIBLE"){
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;

        	}
        	//2
        	cur="";
        	rtem = r;
        	ytem = y;
        	btem  = b;
        	while(rtem>=0 || ytem>=0 || btem>=0){
        		if(rtem < 0 || ytem <0 || btem < 0)break;
        			if(!rtem && !ytem && prev == 2)break;
        			if(!btem && !ytem && prev == 0)break;
        			if(!rtem && !btem && prev == 1)break;
        			if(ytem>=rtem && ytem>=btem && prev!=1){
        				cur+='Y';
        				prev = 1;
        				ytem--;
        				continue;
        			}
        			if(rtem>=ytem && rtem>=btem && prev!=0){
        				cur+='R';
        				prev = 0;
        				rtem--;
        				continue;
        			}
        			
        			if(btem>=rtem && btem>=ytem && prev!=2){
        				cur+='B';
        				prev = 2;
        				btem--;
        				continue;
        			}
        			if(prev == 1){
        				if(rtem>btem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				} }
        			if(prev == 0){
        				if(ytem>btem){
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				}}
        			
        			if(prev == 2){
        				if(rtem>ytem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        			}
        			break;



        	}
        	 pos = true;
        	 ans="";
        	for(int i = 0;i<cur.size() - 1;i++){
        		if(cur[i] == cur[i+1])pos = false;
        	}
        	if(cur[0] ==  cur[cur.size() - 1])pos = false;
        	if(pos && cur.size() == n){
        		ans = cur;
        	}
        	else ans ="IMPOSSIBLE";
        	if(ans != "IMPOSSIBLE"){
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;

        	}
        	//3
        	cur="";
        	rtem = r;
        	ytem = y;
        	btem  = b;
        	while(rtem>=0 || ytem>=0 || btem>=0){
        		if(rtem < 0 || ytem <0 || btem < 0)break;
        		if(!rtem && !ytem && prev == 2)break;
        			if(!btem && !ytem && prev == 0)break;
        			if(!rtem && !btem && prev == 1)break;
        			if(rtem>=ytem && rtem>=btem && prev!=0){
        				cur+='R';
        				prev = 0;
        				rtem--;
        				continue;
        			}
        			if(btem>=rtem && btem>=ytem && prev!=2){
        				cur+='B';
        				prev = 2;
        				btem--;
        				continue;
        			}
        			if(ytem>=rtem && ytem>=btem && prev!=1){
        				cur+='Y';
        				prev = 1;
        				ytem--;
        				continue;
        			}
        			
        			if(prev == 0){
        				if(ytem>btem){
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				}}
        			
        			if(prev == 2){
        				if(rtem>ytem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        			}
        			if(prev == 1){
        				if(rtem>btem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				} }
        			break;



        	}
        	 pos = true;
        	 ans="";
        	for(int i = 0;i<cur.size() - 1;i++){
        		if(cur[i] == cur[i+1])pos = false;
        	}
        	if(cur[0] ==  cur[cur.size() - 1])pos = false;
        	if(pos && cur.size() == n){
        		ans = cur;
        	}
        	else ans ="IMPOSSIBLE";
        	if(ans != "IMPOSSIBLE"){
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;

        	}
        	//4
        	cur="";
        	rtem = r;
        	ytem = y;
        	btem  = b;
        	while(rtem>=0 || ytem>=0 || btem>=0){
        		if(rtem < 0 || ytem <0 || btem < 0)break;
        			if(!rtem && !ytem && prev == 2)break;
        			if(!btem && !ytem && prev == 0)break;
        			if(!rtem && !btem && prev == 1)break;
        			if(ytem>=rtem && ytem>=btem && prev!=1){
        				cur+='Y';
        				prev = 1;
        				ytem--;
        				continue;
        			}
        			if(btem>=rtem && btem>=ytem && prev!=2){
        				cur+='B';
        				prev = 2;
        				btem--;
        				continue;
        			}
        			if(rtem>=ytem && rtem>=btem && prev!=0){
        				cur+='R';
        				prev = 0;
        				rtem--;
        				continue;
        			}
        			
        			
        			
        			if(prev == 1){
        				if(rtem>btem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				} }
        			if(prev == 2){
        				if(rtem>ytem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        			}
        			if(prev == 0){
        				if(ytem>btem){
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				}}
        			break;



        	}
        	 pos = true;
        	 ans="";
        	for(int i = 0;i<cur.size() - 1;i++){
        		if(cur[i] == cur[i+1])pos = false;
        	}
        	if(cur[0] ==  cur[cur.size() - 1])pos = false;
        	if(pos && cur.size() == n){
        		ans = cur;
        	}
        	else ans ="IMPOSSIBLE";
        	if(ans != "IMPOSSIBLE"){
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;

        	}
        	//5
        	cur="";
        	rtem = r;
        	ytem = y;
        	btem  = b;
        	while(rtem>=0 || ytem>=0 || btem>=0){
        		if(rtem < 0 || ytem <0 || btem < 0)break;
        		if(!rtem && !ytem && prev == 2)break;
        			if(!btem && !ytem && prev == 0)break;
        			if(!rtem && !btem && prev == 1)break;
        		if(btem>=rtem && btem>=ytem && prev!=2){
        				cur+='B';
        				prev = 2;
        				btem--;
        				continue;
        			}
        			if(rtem>=ytem && rtem>=btem && prev!=0){
        				cur+='R';
        				prev = 0;
        				rtem--;
        				continue;
        			}
        			if(ytem>=rtem && ytem>=btem && prev!=1){
        				cur+='Y';
        				prev = 1;
        				ytem--;
        				continue;
        			}
        			if(prev == 2){
        				if(rtem>ytem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        			}
        			
        			if(prev == 0){
        				if(ytem>btem){
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				}}
        			if(prev == 1){
        				if(rtem>btem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				} }
        			
        			break;



        	}
        	 pos = true;
        	 ans="";
        	for(int i = 0;i<cur.size() - 1;i++){
        		if(cur[i] == cur[i+1])pos = false;
        	}
        	if(cur[0] ==  cur[cur.size() - 1])pos = false;
        	if(pos && cur.size() == n){
        		ans = cur;
        	}
        	else ans ="IMPOSSIBLE";
        	if(ans != "IMPOSSIBLE"){
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;

        	}
        	//6
        	cur="";
        	ans="";
        	rtem = r;
        	ytem = y;
        	btem  = b;
        	while(rtem>=0 || ytem>=0 || btem>=0){
        		if(rtem < 0 || ytem <0 || btem < 0)break;
        		if(rtem < 0 || ytem <0 || btem < 0)break;
        			if(!rtem && !ytem && prev == 2)break;
        			if(!btem && !ytem && prev == 0)break;
        			if(!rtem && !btem && prev == 1)break;
        			if(btem>=rtem && btem>=ytem && prev!=2){
        				cur+='B';
        				prev = 2;
        				btem--;
        				continue;
        			}
        			
        			if(ytem>=rtem && ytem>=btem && prev!=1){
        				cur+='Y';
        				prev = 1;
        				ytem--;
        				continue;
        			}
        			
        			if(rtem>=ytem && rtem>=btem && prev!=0){
        				cur+='R';
        				prev = 0;
        				rtem--;
        				continue;
        			}
        			if(prev == 2){
        				if(rtem>ytem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        			}
        			
        			if(prev == 1){
        				if(rtem>btem){
        					cur+='R';rtem--;prev = 0;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				} }
        			if(prev == 0){
        				if(ytem>btem){
        					cur+='Y';ytem--;prev = 1;continue;
        				}
        				else{
        					cur+='B';btem--;prev = 2;continue;
        				}}
        			
        			break;



        	}
        	 pos = true;
        	 ans="";
        	for(int i = 0;i<cur.size() - 1;i++){
        		if(cur[i] == cur[i+1])pos = false;
        	}
        	if(cur[0] ==  cur[cur.size() - 1])pos = false;
        	if(pos && cur.size() == n){
        		ans = cur;
        	}
        	else ans ="IMPOSSIBLE";
        	if(ans != "IMPOSSIBLE"){
        		cout<<"Case #"<<yi+1<<": "<<ans<<"\n";
        		continue;

        	}


        	ans = "IMPOSSIBLE";
        cout<<"Case #"<<yi+1<<": "<<ans<<"\n";



}




return 0;}

