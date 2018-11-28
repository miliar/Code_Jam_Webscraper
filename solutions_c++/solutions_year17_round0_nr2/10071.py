#include<iostream>
#include<string>
#include<fstream>
using namespace std;
/*string s1;

int check(){
    cout<<"check called"<<endl;
    int flag = 1;
    for(int i=0;i<s1.length()-2;i++){
        if(s1[i] > s1[i+1]){
            flag = 1;
            break;
        }
    }
    if(flag == 1)
        return 1;
    else
        return 0;

}
void decrease(){
    cout<<"decrease called"<<endl;
    int i = s1.length()-1;
    int tem = int(s1[i]);
        tem--;
        s1[i] = int(tem);
    while(s1[i] == 0){
        int temp = s1[i-1];
        temp--;
        s1[i-1] = int(temp);
        i--;
    }
}
int main(){
    int t,j,k;
    cin>>t;
    for(j=0;j<t;j++){
        cin>>s1;

        cout<<endl;
        while(true){
            k = check();
            if(k == 0){
                cout<<s1<<endl;
                continue;
            }else{
                decrease();
            }
            for(int f = 0;f<s1.length();f++)
            cout<<s1[f];
        }

        cout<<"j loop"<<endl;
    }
}*/

int check(int n){
    unsigned long long int x = (n/10);
    while(x){
        //cout<<"check while loop "<<n<<endl;
        unsigned long long int temp1,temp2,b,c;
        temp1 = n%10;
        b = n/10;
        temp2 = b%10;
        //cout<<"temp 1 :"<<temp1<<" temp 2 : "<<temp2<<endl;
        if(temp2 > temp1){
            return 0;
            break;
        }
        n/=10;
        x = n/10;
    }
    return 1;
}
int main(){
    ifstream in("B-small.in");
    ofstream out("B-small.out");
    unsigned long long int a,i,j,k,n,t;
    in>>t;
    for(i=1; i<=t;i++){
        in>>n;
        while(true){
            //cout<<"while loop "<<n<<endl;
            a = check(n);
            //cout<<"a : "<<a<<endl;
            if(a == 1){
                out<<"Case #"<<i<<": "<<n<<endl;
                break;
            }else{
                n--;
            }
        }
    }

}
