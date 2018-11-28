#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin >> t;
	for(int z=1;z<=t;z++){
		string s;
		int k;
		int j,flag=0;
		cin >> s >> k;
			int i=0;
		int count=0;

		while(s[i+k-1]!='\0'){

			if(s[i]=='-'){
				count++;
				for(j=i;j<k+i;j++){
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
			}
			i++;
		}
		i=0;
		while(s[i]!='\0'){
			if(s[i]=='-')
				flag=1;
			i++;  
		}
		if(flag==1)
			cout << "Case #" << z << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << z << ": " << count << endl; 
	}
}
