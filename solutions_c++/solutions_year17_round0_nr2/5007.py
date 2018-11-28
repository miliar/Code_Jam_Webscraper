#include <bits/stdc++.h>

using namespace std;
int main(){
	
	freopen("input2.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin >> t;



	for(int z=1;z<=t;z++){
		string s;
		cin >> s;
		int pt1=0,pt2=0;
		
		int i=0;
		int flag=0;

		if(s.size()==1){
			cout << "Case #" << z << ": " << s << endl;
			continue;
		}

		while(s[i+1]!='\0'){
			if(s[i]<s[i+1]){
				pt1=pt2=i+1;
			}
			else if(s[i]==s[i+1])
				pt2++;	
			else{
				if(pt2==pt1){
					s[i]--;
					i++;
					flag=1;
					break;
				}
				else{
					s[pt1]--;
					i=pt1+1;
					flag=1;
					break;
				}
			}
			i++;
		}


		if(flag==1){
			while(s[i]!='\0')
				s[i++]='9';
		}

		i=0;
		while(s[i]!='\0'){
			if(s[i]!='0')
				break;
			i++;
		}
		cout << "Case #" << z << ": ";
		while(s[i]!='\0'){
			cout << s[i];
			i++;
		}
		cout << endl;



	}
}