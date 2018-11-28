#include <iostream>
#include <algorithm>
using namespace std;
int tt;
string cuttingString(string input){
	string temp=input;
	while(temp[0]=='+'){
		temp.erase(0,1);
	}
	while(temp[temp.length()-1]=='+'){
		temp.erase(temp.length()-1);
	}
	return temp;

}
string changeString(string input,int k,int m){
	string temp=input;
	if((k+m)<=input.length()){
	for (int i = k; i < k+m; ++i)
	{
			if(temp[i]=='+'){
				temp[i]='-';
			}
		else{
			temp[i]='+';
		}
	}
}
	return temp;
}
bool checkComplete(string input){
	size_t found = input.find_first_of('-');
	return (found==string::npos);
}

int times(string input,int k){
	int count=0;
	string temp=cuttingString(input);
	//string temp=input;
	while(checkComplete(temp)==0){
		//cout<<"string: "<<temp<<endl;
		size_t found = temp.find_first_of('-');
		//cout<<"found: "<<found<<" k:"<<k<< endl;
		temp=changeString(temp,found,k);
		temp=cuttingString(temp);
		count++;
		//cout<<temp<<endl;
		if(temp.length()>0 && temp.length()<k){
			return -1;
			break;
		}
}
	return count;
}

/*int possibleNumber(string s){
	size_t found = s.find_first_of(' ');
	int sum=0;
	for (int i = s.length()-1; i >found; i--)
	{
		sum+=((int)s[i]-'0')*pow(10,s.length()-1-i);
	}
return sum;
}
*/
int main() {
	freopen("A-small-attempt3.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &tt);
    string str;
    int num;
    for (int i = 0;i<tt;i++)
     {
     	cin>>str;
     	cin>>num;
     	cout<<"Case #"<<i+1<<": ";
     	if(times(str,num)==-1){
     		cout<<"IMPOSSIBLE"<<endl;
     	}
     	else{
     		cout<<times(str,num)<<endl;
     	}

     } 

//    cout<<times("+--+",2);
    //cout<<"tt:"<<tt;
/*    string myStr="hello";
    cout<<myStr[myStr.length()-1];
*/
	
    return 0;
}