#include <bits/stdc++.h>

using namespace std;

char num[21];

string solve(){

	int n=strlen(num);
	int t, d, pos=n-1;
	string res="";
	bool termino=false;
	for(int i=1; i<n && !termino; i++){
		if(num[i-1]>num[i]){
			d=(int)(num[i-1]-'0');
			d--;
			t=n-i;
			num[i-1]=(char)(d+'0');
			pos=i-1;
            termino=true;
        }
		//cout<<i<<"/"<<res<<endl;
	}
	//printf("cad..%s, res=%s\n", num, res.c_str());
    if(termino){
        string cad(t, '9');
        res+=cad;
    }
    for(int i=pos; i>=1; i--){
        if(num[i-1]>num[i]){
            d=(int)(num[i-1]-'0');
            d--;
            res='9'+res;
            num[i-1]=(char)(d+'0');
        }
        else    res=num[i]+res;
    }
    res=num[0]+res;
    string ans="";
    for(int i=0; i<res.size(); i++){
        if(res[i]!='0'){
            pos=i;
            break;
        }
    }
    res=res.substr(pos);
    return res;
}

int main(){
	int test, u;
	freopen("b2_in.in", "r", stdin);
	freopen("b22_out.txt", "w", stdout);
	scanf("%d", &test);
    string ans;
	for(int tt=1; tt<=test; tt++){
		scanf("%s", &num);
		ans=solve();
		printf("Case #%d: %s\n", tt, ans.c_str());
	}
	return 0;
}
