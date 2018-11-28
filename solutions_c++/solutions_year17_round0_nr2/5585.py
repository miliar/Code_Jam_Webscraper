#include<bits/stdc++.h>
using namespace std;

bool tidy(int n){
    string s="";
    while(n>0){
        s += ('0'+n%10);
        n = n/10;
    }
    reverse(s.begin(),s.end());
    for(int i=0;i<s.length()-1;i++){
        if(s[i]>s[i+1])
            return false;
    }
    return true;
}
int main()
{
    int t;
    ifstream in;
    in.open("B-large.in");
    in >> t;
    ofstream out;
    out.open("result.txt");
    for(int cs=0;cs<t;cs++){
        long long n;
        in >> n;
        string s = "";
        long long m = n;
        while(m>0){
            s += ('0' + m%10);
            m = m/10;
        }
        reverse(s.begin(),s.end());
//        cout<<s<<endl;
        for(int i=0;i<int(s.length())-1;i++){
            if(s[i]<=s[i+1]){
                continue;
            }
            else if(s[i+1]=='0'){
                int upto = s.length();
                if(s[i]=='1'){
                    upto--;
                    int j=i-1;
                    while(s[j]=='1' && j>=0){
                        s[j]='9';
                        j--;
                    }
                }
                else{
                    s[i] = '0' + ((s[i]-'0')-1);
                    int j=i;
    //                cout<<j<<" "<<s[j]<<" "<<s[j-1]<<endl;
                    while(j>0 && s[j]<s[j-1]){
                        s[j-1] = s[j];
                        j--;
                    }
                    i=j+1;
                }
                while(i<upto){
                    s[i] = '9';
                    i++;
                }
                if(upto<s.length())
                    s.erase(s.begin()+int(s.length())-1);
            }
            else{
                int num = (s[i]-'0')*10 + (s[i+1]-'0');
                while(num>0){
                    if(tidy(num)){
                        break;
                    }
                    num--;
                }
                s[i+1] = '0'+ num%10;
                s[i] = '0'+ num/10;
                int j=i;
//                cout<<j<<" "<<s[j]<<" "<<s[j-1]<<endl;
                int flag=0;
                while(j>0 && s[j]<s[j-1]){
                    s[j-1] = s[j];
                    j--;
                    flag=1;
                }
                if(flag==0)
                    i=i+2;
                else
                    i=j+1;
                while(i<int(s.length())){
                    s[i] = '9';
                    i++;
                }
            }

        }
        out<<"Case #"<<cs+1<<": "<<s<<endl;
    }
    return 0;
}

