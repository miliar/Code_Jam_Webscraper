#include<vector>
#include<cstdio>
using namespace std;

vector<int> v;

int main()
{
  int T;
  scanf("%d", &T);
  getchar();
  for(int t=1; t<=T; t++) {
    v.clear();
    char c;
    int find = false;
    while((c=getchar()) && c!='\n') {
      int x = c-'0';
      if(find) v.push_back(9);
      else {
        v.push_back(x);
        if(v.size() > 1)
          for(vector<int>::iterator it=v.end()-1; it!=v.begin(); it--) {
            if(*(it-1)>*it) {
              *it = 9;
              *(it-1) -= 1;
              find = true;
            } else break;
          }
      }
    }
    printf("Case #%d: ", t);
    for(int i=0; i<v.size(); i++)
      if(v[i]>0)
        printf("%d", v[i]);
    putchar('\n');
  }
}
