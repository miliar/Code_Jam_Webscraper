    #include<bits/stdc++.h>
    using namespace std;
    typedef long long ll ;

    int main(){
    ifstream fin ("A-large.in");
    ofstream fout ("outputss.txt");
    if(!fin.is_open()) cout<<"the input file didn't open "<<endl;
    if(!fout.is_open()) cout<<"the output file didn't open " <<endl;
    int t;
    fin>>t;
    for(int tt=1;tt<=t;tt++){

        string s; fin>>s ;

       int n,l,ans=0;
       fin>> n ;

       l = s.size();
       for(int i=0 ;i<=(l-n) ; i++){
            if(s[i] == '-'){
                ans++;
                for(int j=i ; j<i+n ; j++){
                     if(s[j]=='-') s[j] = '+';
                     else s[j] = '-';
                }
            }
       }
      // printf("%d\n",ans);
       for(int i=(l-n+1) ; i<l ; i++){
          if(s[i] == '-'){
              ans = -1 ;
              break ;
          }
       }

      if(ans != -1) fout<<"Case #"<<tt<<": "<<ans<<endl;
      else  fout<<"Case #"<<tt<<": IMPOSSIBLE"<<endl;
    }
    fin.close();
  fout.close();
       return 0 ;
    }
