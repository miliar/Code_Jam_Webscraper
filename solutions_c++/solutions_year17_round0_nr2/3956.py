#include"iostream"
#include"string"

using namespace std;

int main(){
    int times,t=0;
    cin >> times;
    while(times--){
      t++;
      string s;
      cin >> s;
      int same=0;
      char pre = s[0];
      for(int a=1;a<s.length();a++){
        if(s[a]<pre){
          s[same]--;
          for(int b=same+1;b<s.length();b++)s[b]='9';
          break;
        }else if(s[a]!=pre)same=a;
        pre=s[a];
      }
      cout << "Case #" << t << ": ";
      int first=1;
      for(int a=0;a<s.length();a++){
        if(first==1 && s[a]=='0')continue;
        first=0;
        cout<<s[a];
      }
      cout<<endl;
    }
    return 0;
}
