#include<bits/stdc++.h>

using namespace std;

bool ap(int n){
	if(n/10 > n%10)
		return false;
	return true;
}

int main(){
	int mem[100];
	int count = 0;
	mem[0] = 99;
	
	for(int i = 1; i < 100; i++){
		if(ap(i))
			mem[i] = i;
		else
			mem[i] =  mem[i-1];
	}
	
	//for(int i = 0; i < 100; i++)
		//printf("%d : %d\n", i, mem[i]);
	
	int t;
	
	scanf("%d ", &t);
	
	while(t--){
		count++;
		string s;
		
		cin >> s;
		
		for(int i = 0;  i < s.size() - 1; i++){
			if(s[i] > s[i+1]){
				int n = (s[i] - '0')*10 + (s[i+1] - '0');
				s[i + 1] = mem[n]%10 + '0';
				s[i] = mem[n]/10 + '0';
			
				for(int j = i + 2; j < s.size(); j++)
					s[j] = '9';
				
				for(int j = i - 1; j >= 0; j--)
					if(s[j] > s[i]){
						s[j]--;
						for(int k = j + 1; k < s.size(); k++)
							s[k] = '9';
					}
				
				break;
			}
			
		}
		
		//cout << "s: " << s << endl;
		
		int fz = 0;
		
		printf("Case #%d: ", count);
		
		for(int i = 0; i < s.size(); i++){
			if(s[i] != '0'){
				printf("%c", s[i]);
				fz = 1;
			}
			else{
				if(fz == 1)
					printf("0");
			}
		}
		printf("\n");
	}
	
	return 0;
}