#include<bits/stdc++.h>
#define mpr make_pair
#define ff first
#define ss second
#define pb push_back
#define ll long long 
using namespace std;

typedef priority_queue<pair<int,pair<int,int> >,vector<pair<int,pair<int,int> > >, std::greater<pair<int,pair<int,int> > > > PQ;

//scanf ("%[^\n]%*c",inp);


int getPlus(string str){
	
	int ct=0;
	for(int i=0;i<str.size();i++){
		if(str[i]=='+')
			ct++;
	}
	
	return ct;
	
}


void flip(string &str,int st,int end){
	
	
	for(int i=st;i<=end;i++){
		
		if(str[i]=='+')
			str[i]='-';
		else
			str[i]='+';
	}
	
	
}

int main(){
	
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	
	
	int te,t=1;
	scanf("%d\n",&te);
	
	while(t<=te){
		
		string str;
		int k;
		
		cin>>str;
		cin>>k;
		int flips=0;
		for(int i=0;i<str.size()-(k-1);i++){
			
			if(str[i]=='+')
				continue;
			else{
				flip(str,i,i+k-1);
				flips++;
			}
			
		}
		
		if(getPlus(str)==str.size()){
			cout<<"Case #"<<t<<": "<<flips<<endl;
		}
		else{
			cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		}
	
	t++;
	}

return 0;	
}

