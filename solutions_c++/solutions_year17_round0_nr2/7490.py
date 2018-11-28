#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A1.in","r",stdin);
   	freopen("A2.out","w",stdout);
	int t;
	cin>>t;
	for(int tt = 1 ; tt <= t ; tt++)
	{
		cout<<"Case #"<<tt<<": ";
		string s;
		
		int flag = 0;
		cin>>s;
		if(s.size() == 1){
			cout<<s[0]<<endl;
			continue;
		}		
		int i;
		for(i = 0 ; i < s.size() - 1 ; i++){
			if(s[i] > s[i + 1]){
				if(s[i] == '1'){
					flag = 1;
					break;
				}	
				else
					break;
			}
		}
		
		if(i == s.size() - 1){
			for(int i = 0 ; i < s.size() ; i++){
				cout<<s[i];
			}	
		}
		else if(flag == 1)
		{
			for(int i = 0 ; i < s.size() - 1 ; i++){
				cout<<"9";
			}
		}
		else{
			int j;
			
			for(j = i ; j > 0 ; j--){
				if(s[j] != s[j - 1]){
					break;
				}
			}

			s[j]--;
			int k;
			for(k = 0 ; k <= j ; k++){
				cout<<s[k];
			}
			for(int l = 0 ; l < s.size() - k ; l++){
				cout<<"9";
			}	
		}

		cout<<endl;
		
	}
}