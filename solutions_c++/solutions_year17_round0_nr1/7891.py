#include<bits/stdc++.h>

using namespace std;

int main(){
	int t,x,k,i,j,c,c2,f;
	string str,str2;
	freopen("q1.in","r",stdin);
	freopen("q1.out","w",stdout);
	cin>>t;
	for(int x=1;x<=t;x++){
		cin>>str>>k;
		str2=str;
		c=c2=i=0;
		while(i<str.length()){
			while(str[i]=='+'){ i++; if (i>=str.length()) break;	}
			if(i>=str.length()) break;
			f=1;
			for(j=i;j<i+k;j++){
				if(j>=str.length()) { f=0; break; }
				if(str[j]=='+') str[j]='-';
				else str[j]='+';
			}
			if(f==1) c++;
			else {c=-1; break;}
		}

		i=str2.length()-1;
		while(i>=0){
			while(str2[i]=='+'){ i--; if (i<0) break;	}
			if(i<0) break;
			f=1;
			for(j=i;j>i-k;j--){
				if(j<0) { f=0; break; }
				if(str2[j]=='+') str2[j]='-';
				else str2[j]='+';
			}
			if(f==1) c2++;
			else {c2=-1; break;}
		}
		if(c==-1 && c2==-1) cout<<"Case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
		else if(c==-1) cout<<"Case #"<<x<<": "<<c2<<endl;
		else if(c2==-1) cout<<"Case #"<<x<<": "<<c<<endl;
		else if(c<c2) cout<<"Case #"<<x<<": "<<c<<endl;
		else cout<<"Case #"<<x<<": "<<c<<endl;
	}
	return 0;
}