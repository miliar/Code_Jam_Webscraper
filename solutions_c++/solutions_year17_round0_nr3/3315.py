#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main(int argc, char const *argv[])
{
	FILE * sFileIn;
	FILE * sFileOut;
	int    sDataCnt;
        long long    stall, people;
        long long    min,max;
        int i;

	sFileIn  = fopen( "C-large.in.txt", "r");
	sFileOut = fopen( "C-large.out.txt", "w+");

	fscanf( sFileIn, "%d\n", &sDataCnt );

        for( i = 1 ; i <= sDataCnt ; i++ )
	{
            fscanf( sFileIn, "%lld %lld\n", &stall, &people );

            printf("Case #%d: %lld %lld - ", i, stall, people);

            //people--;
            while( people > 1 )
            {
                if(( ( stall % 2 ) == 0 ) && ( ( people% 2 ) == 1 )) stall--;
                people = people/2;
                stall  = stall/2;
            }

            stall--;
            min = stall/2;
            max = min + ( stall % 2 );

            printf(" %lld %lld\n", max, min);
            fprintf(sFileOut,"Case #%d: %lld %lld\n", i, max, min);
        }

        fclose(sFileIn);
	fclose(sFileOut);

	return 0;
}
