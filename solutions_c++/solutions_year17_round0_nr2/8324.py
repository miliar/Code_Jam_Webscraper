#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
bool isTidy(unsigned long long n){
    if(n/10 == 0)
        return true;
    else{
        unsigned long long t = n;
        int prev = t%10;
        int next;
        t = t / 10;
        while(t){
            next = t % 10;
            if (next > prev){
                return false;
            }
            t = t / 10;
            prev = next;
        }
        return true;
    }
}

int getTidySlow(int n){
    if( n/10 == 0 ){
        return n;
    }
    n++;
    while(n--){
        int t = n;
        int prev;
        prev = t%10;
        t = t / 10;
        int next;
        bool flag = true;
        while(t){
            next = t % 10;
            if (prev < next){
                flag = false;
                break;
            }
            prev = next;
            t = t / 10;
        }
        if(flag)
            return n;
    }
}

unsigned long long getTidy(unsigned long long n){
    if(!n)return n;
    vector<int> digits;
    unsigned long long t = n;
    while(t){
        //cout<<t%10;
        digits.push_back(t%10);
        t = t / 10;
    }
    int i;
    bool flag = true;
    //cout<<"before change"<<endl;
    for (int i = 0; i< digits.size();i++){
        //cout<<digits[i];
    }
    //cout<<endl;
    for( i = digits.size()-1;i>0 ;i-- ){
        //cout<<"digits"<<digits[i]<<endl;
        if(digits[i] > digits[i-1]){
            //cout<<"this digit is greater than the lower"<<endl;
            digits[i] = digits[i] - 1;
            //cout<<"digit after changing"<<digits[i]<<endl;
            flag = false;
            break;
        }
    }
    //cout<<"index "<<i<<endl;
    if(!flag){
        for (int j = i-1; j>=0;j--){
            digits[j] = 9;
        }
    }
    //cout<<"after change operation"<<endl;
    for (int i = 0; i< digits.size();i++){
        //cout<<digits[i];
    }
    unsigned long long tidy = digits[digits.size() - 1];
    //cout<<tidy<<endl;
    for (int j = digits.size() - 2; j >= 0; j--){
        tidy = tidy*10 + digits[j];
    }
    //return tidy;
    if(isTidy(tidy))
        return tidy;
    else
        return getTidy(tidy);
    
}
int main(){
    int t;
    unsigned long long n;
    cin>>t;
    int i = 0;
    /*while(1){
        n = rand() % 1001;
        cout<<n<<endl;
        int op1 = getTidy(n);
        int op2 = getTidySlow(n);
        cout<<op1<<endl<<op2<<endl<<endl<<endl;;
        if ( op1 != op2 ){
            cout<<"this is the wrong test case"<<endl;
            cout<<"number "<<n<<endl;
            cout<<"getTidy "<<op1<<endl;
            cout<<"Gettidy brute "<<op2<<endl;
            return 0;
        }
    }*/

    while(t--){
        cin>>n;
        cout<<"Case #"<<i++ + 1<<": "<<getTidy(n)<<endl;
    }
}
