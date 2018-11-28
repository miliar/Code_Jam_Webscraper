#include <iostream>
using namespace std;

int no;
int sol;

int main(int argc, char* argv[]) {
  int TEST_FROM = 0;
  int TEST_TO = 123456789;
  /*if (argc == 3) {
    sscanf(argv[1], "%d", &TEST_FROM);
    sscanf(argv[2], "%d", &TEST_TO);
  }*/
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    // input data starts
    scanf("%d", &no);
    
    //solution starts
    printf("Case #%d: ", qq);
    fflush(stdout);
    
     int x;
    int rem=0;
    int rem2;
    
    do
    {
        sol=1;
        x=no;
        while(x>0)
        {
            rem2=x%10;
            x=x/10;
            rem=x%10;
            if(rem>rem2)
            {
                sol=0;
                no--;
                break;
            }       
        }
        
    }while(sol==0);
    
    printf("%d\n", no);
    // solution ends
    fflush(stdout);
    //fprintf(stderr, "test %d solved, time = %d ms\n", qq, (int)clock());
  }
  return 0;
}
