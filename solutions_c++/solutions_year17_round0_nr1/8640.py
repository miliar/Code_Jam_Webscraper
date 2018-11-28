#include <vector>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;


string itos(int a){
	string res;
	
	if(!a)
		return "0";
		
	while(a){
		res+=a%10+'0';
		a/=10;
	}
	reverse(res.begin(),res.end());
	return res;
}

char rev(char c){
	if(c=='+')
		return '-';
		
	return '+';
}


int main(){
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("myff","w",stdout);
	int i,q,k,t,j,l;
	
	cin>>t;
	string c, x;
	for(q = 1; q<=t; q++){
		queue<string> aa,bb, *a,*b;
		a=&aa;b=&bb;
		set<string> s;
		cin>>c;
		cin>>k;
		string rr = "IMPOSSIBLE";
		string res;
		
		int i = 0;
		aa.push(c);
		
		for(j = 0; j < c.size(); j ++)
			res+='+';
			
		bool brk = false;
		
		
		while(!a->empty()){
			
			while(!a->empty()){
			
			x = a->front();
			a->pop();
			//cout<<x<<endl;
			//cout<<i<<" "<<x<<endl;
			if(x==res){
				//cout<<" I JE "<<i<<endl;
				rr = itos(i);
				brk = true;
				break;
			}
				
							
			if(s.find(x)!=s.end())
				continue;
			
			
			s.insert(x);
			
			
			for(j = 0; j+k<=res.size(); j++){
				string ppp=x;
				for(l = j; l<j+k;l++)
					x[l] = rev(x[l]);
				
				if(s.find(x)==s.end()){
			//		if(i==2 && ppp=="++++---+")
			//			cout<<j<<" "<<k<<" "<<res.size()<<" "<<x<<" "<<(s.find("++++++++")==s.end())<<endl;
					b->push(x);
				}
					
				
				for(l = j; l<j+k;l++)
					x[l] = rev(x[l]);
				
			}
			
		}
		if(brk)
				break;
			swap(a,b);
			i++;
			
		}
		
		cout<<"Case #"<<q<<": "<<rr<<endl;
		
	}
	
	
	
	return 0;
	
}
