#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    int case_num=0;

    while(scanf("%d",&case_num)!=EOF && case_num)
    {
        for(int i=1;i<=case_num;++i){
            char input[20];
            scanf("%s",input);
            int len = strlen(input);

            //int temp=input;
            for(int j=len-1;j>=1;){
                if(input[j]<input[j-1]){
                    input[len-1]--;
                    //printf("A%d in:%s\n",j,input);
                    for(int k=len-1;k>=0;--k){
                        if(input[k]<'0'){
                            input[k] += 10;
                            input[k-1] -= 1;
                            //printf("B%d in:%s\n",k,input);
                        }
                        else
                            break;
                    }

                }
                else
                    --j;
                //printf("%d out:%s\n",j,input);
            }
            printf("Case #%d: ",i);
            int temp=0;
            for(int j=0;j<len;++j)
                if(input[j]!='0'){
                    temp = j;
                    break;
                }
            for(int j=temp;j<len;++j)
                printf("%c",input[j]);
            //if(i!=case_num)
                printf("\n");


        }
    }

    return 0;
}
