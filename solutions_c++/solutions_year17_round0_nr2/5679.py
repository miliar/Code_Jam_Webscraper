#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
int testcase;
cin>>testcase;
int answer=0;
while(testcase--){
	answer++;
	string string_s;
	cin>>string_s;
	
	int len =string_s.size();
	
	int case_value=0;

 	// finding whether string is already sorted or not ....

	for(int i=0;i<len-1;i++){
		// if previous index value is greater then we find atleast one inversion 
		if(string_s[i]>string_s[i+1]){
			case_value=1;
			break;
		}
	}
	// if no inversion then Number is already tidy
	if(case_value==0){	
	   cout<<"Case #"<<answer<<": "<<string_s<<"\n";
	}
        // else we have to make it tidy.
	else{ int flag=1;
                while(flag){
		for(int i=0;i<len-1;i++){
			// finding first inversion and then start making number tidy.
			if(string_s[i]>string_s[i+1]){
				flag=1;
				string_s[i]=string_s[i]-1;
				for(int j=i+1;j<len;j++)
					string_s[j]='9';
				break;
			}
                         else{flag=0;}
                  
		}
             }

// deleting the leading zero..
		if(string_s[0]=='0'){
			cout<<"Case #"<<answer<<": ";
			
			for(int i=1;i<len;i++)
			  cout<<string_s[i];
		cout<<endl;
		}
		else
	           cout<<"Case #"<<answer<<": "<<string_s<<endl;
	}
}
}
