#include<bits/stdc++.h>

using namespace std;
int toString(char a[]) {
  int c, sign, offset, n;

  if (a[0] == '-') {
  }

  if (sign == -1) {
    offset = 1;
  }
  else {
    offset = 0;
  }

  n = 0;

  for (c = offset; a[c] != '\0'; c++) {
    n = n * 10 + a[c] - '0';
  }

  if (sign == -1) {
    n = -n;
  }

  return n;
}
int fast_atoi( const char * str )
{
    int val = 0;
    while( *str ) {
        val = val*10 + (*str++ - '0');
    }
    return val;
}
int main(){

freopen("A-large.in","r",stdin);

freopen("A-large.out","w",stdout);

int t;
cin>>t;

string a[2*t];

for(int i=0;i<2*t;i++){
    cin>>a[i];

}

for(int i=0;i<2*t;i+=2)
{
    string s=a[i];
    int k=fast_atoi(a[i+1].c_str());
    int out=0;
    for(int j=0;j<s.length();j++){

       if(j+k<=s.length()){
      if(s[j]=='-'){
        int temp=0;
        while(temp<k)
        {
            if(s[j+temp]=='+')
                s[j+temp]='-';
            else
                s[j+temp]='+';
        temp++;
        }
        out++;
      }

       }

    }
    if(s.find('-')>s.length())
        cout<<"Case "<<"#"<<i/2+1<<": "<<out<<endl;
    else
        cout<<"Case "<<"#"<<i/2+1<<": "<<"IMPOSSIBLE"<<endl;

}


}
