#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int main(){
	int T;
	long long N;


  	freopen ("B-large.in","r",stdin);
  	freopen("B-large-output", "w", stdout);

//Getting number of times
	scanf("%d", &T);


//For each number
	for(int t=1;t<=T;t++){
		vector<int> num;
		
		cin >> N;
		while(N>0){
			num.push_back(N%10);
			N/=10;
		}
		reverse(num.begin(),num.end());
		
		vector<int> diff(num.size(),0);
		for(int i =1; i<num.size(); i++)
			diff[i] = num[i] - num[i-1];
		
		for(int i=0;i<num.size()-1;i++){
			if(num[i] > num[i+1]){
				int j;
				for(j=i;j>0;j--)
					if(diff[j]>0)
						break;
				num[j] --;
				for(int k=j+1;k<num.size();k++)
					num[k]=9;
				break;				
			}
		}
		
		int i;
		for(i=0;i<num.size();i++)
			if(num[i]!=0)
				break;
		printf("Case #%d: ", t);	
		for(int j =i; j<num.size(); j++)
			printf("%d", num[j]);
		printf("\n");		
	}
	
	return 0;
}