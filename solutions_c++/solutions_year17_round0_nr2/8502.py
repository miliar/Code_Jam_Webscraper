#include <bits/stdc++.h>

using namespace std;

int main()
{

   ifstream fin ("B-small-attempt1.in");
    ofstream fout ("outputs.txt");
    if(!fin.is_open()) cout<<"the input file didn't open "<<endl;
    if(!fout.is_open()) cout<<"the output file didn't open " <<endl;
    int t;
    fin>>t;
    for(int j=1;j<=t;j++){
        int n;
        fin>>n;
        while(n){
                bool f=true;
            stringstream ss;
            ss<<n;
            string s;
            s=ss.str();
            for(int i=s.size()-1;i>0;i--){
                if(s[i-1]-'0'>s[i]-'0'){
                    f=false;
                    break;
            }
        }
        if(!f) n--;
        else break;
    }
    fout<<"Case #"<<j<<": "<<n<<endl;
    }
    fin.close();
  fout.close();
    return 0;
}
