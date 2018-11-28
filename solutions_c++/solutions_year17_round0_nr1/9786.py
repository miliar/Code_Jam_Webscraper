#include<iostream>
#include<string>

using namespace std;

//isHappy function is used to find if character at i is '+' or '-'
bool isHappy(char c){
    if(c == '+'){
        return true;
    }
    return false;
}

//isValid function used to find if length of string from i-end
//is more than or equal to k
bool isValid(string s, int k, int i){
    int totalLength = s.length();
    int temp = totalLength - i ;
    if(temp < k) return false;
    else return true;
}

void isConvertible(string s, int k){
	int i = 0;
    int count = 0;
    int length = s.length();
    int sizeOfFlipper = k;
    while(i < length){
        if(isHappy(s[i])){
            i++;
        }else if(!isValid(s, k , i)){
            cout<<"IMPOSSIBLE"<<endl;
            return;
        }else{
            sizeOfFlipper = k;
            int index = i;
            while(sizeOfFlipper--){
                if(s[index] == '+'){
                    s[index] = '-';
                }else{
                    s[index] = '+';
                }
                index++;
            }
            count++;
        }
    }
    if(i == length) cout<<count<<endl;
}

int main(){
    int t;
    cin>>t;
    int i = 1;
    while(t--){
    	string s = "";
    	int k;
        cin>>s>>k;
        cout<<"Case #"<<i<<": ";
    	isConvertible(s, k);
        i++;
    }
    return 0;
}
