#include <cstdio>
#include <iostream>

using namespace std;

int check(char in[], int len) {
  for (int i =1; i<len; i++) {
    if (in[i]<in[i-1])
      return 1;
  }
  return 0;
}

void made(char in[], int len) {
  for (int i = len-1; i>=0; i--) {
    if (in[i]!='9') {
      in[i] = '9';
      int j = i-1;
      while (in[j]=='0') {
        in[j]='9';
        j--;
      }
      // cout<<in[j];
      in[j]--;
      // cout<<">>"<<in[j]<<endl;
      return;
    }
  }
  return;
}

char ch_n[50];
int T;

int main() {
  cin >> T;
  for (int t = 1; t<=T; t++) {
    cin >> ch_n;
    int len_n = strlen(ch_n);
    if (len_n==1 && ch_n[0]=='0') {
      printf("Case #%d: 0\n",t);
      continue;
    }
    while (check(ch_n, len_n)==1) {
      made(ch_n, len_n);
      // cout<<ch_n<<endl;
    }
    int k = 0;
    while (ch_n[k]=='0') k++;
    printf("Case #%d: ",t);
    for (;k<len_n;k++) {
      printf("%c",ch_n[k]);
    }
    printf("\n");
  }
  return 0;
}