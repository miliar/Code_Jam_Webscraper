#include<stdio.h>
#include<stdlib.h>
#include<string.h>



int main(int argc, char const *argv[])
{
	FILE * sFileIn;
	FILE * sFileOut;
	int    sDataCnt;
        char   S[1001];
        char * s;
        int    K;
        int    i,j,k,y;
        int    sLength;
        
	sFileIn  = fopen( "A-small-attempt0.in.txt", "r");
	sFileOut = fopen( "A-small-attempt0.out.txt", "w+");

	fscanf( sFileIn, "%d\n", &sDataCnt );

        printf("%d\n",sDataCnt);

        for( i = 1 ; i <= sDataCnt ; i++ )
	{
            fscanf( sFileIn, "%s %d\n", S, &K );
            sLength = strlen(S);

            //      printf("%s %d %d\n",S, K, sLength);

            for( j = 0,y = 0,s=S ; j <= (sLength - K) ; j++,s++  )
            {
                if( *s == '-')
                {
                    y++;
                    for( k = 0; k < K ; k++)
                    {
                        if(s[k] == '-')  s[k] = '+';
                        else if(s[k] == '+') s[k] = '-';
                        else  printf("invaled %c\n",s[k]);
                    }
                }
            }

            for( j = 0 ; j  < K ; j++)
            {
                if(s[j] == '-')
                {
                    break;
                }
            }
            if(j == K)
            {
                printf("Case #%d: %d\n",i,y);
                fprintf(sFileOut,"Case #%d: %d\n",i,y);
            }
            else
            {
                printf("Case #%d: IMPOSSIBLE\n",i);
                fprintf(sFileOut,"Case #%d: IMPOSSIBLE\n",i);
            }
        }
	fclose(sFileIn);
	fclose(sFileOut);

	return 0;
}
