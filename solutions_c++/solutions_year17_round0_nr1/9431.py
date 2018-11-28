#include<bits/stdc++.h>

using namespace std;
string str;
char rev(char ch){
    if(ch == '-')
    return '+';
    return '-';
}
int main(){
	int t,res,k,i,j,n,test;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> t;

	for(test = 1 ; test <= t; test++){
        res = 0;
		cin>>str;
		cin >> k;
		n = str.size();
		for(i = 0 ; i < n-k+1 ; i++){
			if(str[i] == '-'){
				res++;
				for(j = 0 ; j < k ;j++){
					str[i+j] = rev( str[i+j]);
				}
			}
		}
		i--;
		for(j = 0 ; j < k ;j++)
			if(str[i+j] == '-')
				break;
        cout<<"Case #"<<test<<": ";
		if(j == k)
			cout<<res<<"\n";
		else cout<<"IMPOSSIBLE\n";
	}
	return 0;
}
