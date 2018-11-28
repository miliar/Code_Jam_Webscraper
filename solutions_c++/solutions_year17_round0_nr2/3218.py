#include<stdio.h>
#include<stdlib.h>
#include<string.h>



int main(int argc, char const *argv[])
{
	FILE * sFileIn;
	FILE * sFileOut;
	int    sDataCnt;
        char   number[20];
        int    i,j;
        int    sLength;
        int    nineStart;
        char * numberStart;

	sFileIn  = fopen( "B-large.in.txt", "r");
	sFileOut = fopen( "B-large.out.txt", "w+");

	fscanf( sFileIn, "%d\n", &sDataCnt );

//        printf("%d\n",sDataCnt);

        for( i = 1 ; i <= sDataCnt ; i++ )
	{
            fscanf( sFileIn, "%s\n", number );
            sLength = strlen(number);

            //          printf("%s %d\n",number, sLength);

            nineStart = sLength;
            for( j = sLength-2 ; j >= 0 ; j--  )
            {
                if(number[j]>number[j+1])
                {
                    nineStart = j+1;
                    number[j]--;
                }
            }

            for( j = nineStart ; j< sLength ; j++ )
            {
                number[j] = '9';
            }
            for( j = 0 ; j< sLength ; j++ )
            {
                if(number[j] != '0') break;
            }
            numberStart = number + j;

            printf("Case #%d: %s\n", i, numberStart);
            fprintf(sFileOut,"Case #%d: %s\n", i, numberStart);
        }
	fclose(sFileIn);
	fclose(sFileOut);

	return 0;
}
