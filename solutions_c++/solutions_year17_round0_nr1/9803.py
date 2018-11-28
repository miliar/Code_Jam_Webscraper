#include<iostream>
#include<fstream>
//std::string s;
std::string toggle(std::string s,int i,int k){
    for(int j=i;j<k+i;j++)
    if(s[j]=='-')
        s[j]='+';
    else
        s[j]='-';
    return s;
}
int main(){
    std::ifstream input;
    input.open("input.cpp");
    std::ofstream output;
    output.open("output.cpp");
    int t;
    input>>t;
    for( int tc=0;tc<t;tc++){
        std::string s;
        input>>s;
    int n = s.length();
        int k,c=0,i;
        input>>k;
        for( i=0;i<n-k+1;i++){
            if(s[i]=='-'){
             s = toggle(s,i,k);
                c++;
            }
        }
        for( i=0;i<n;++i){
            if(s[i]=='-')
                break;
        }
        if(i==n)
            output<<"Case #"<<tc+1<<": "<<c<<std::endl;
        else
            output<<"Case #"<<tc+1<<": IMPOSSIBLE"<<std::endl;
    }
    return 0;
}
