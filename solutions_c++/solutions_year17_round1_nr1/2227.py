#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main(int argc, char const *argv[])
{
	FILE * sFileIn;
	FILE * sFileOut;
	int    sDataCnt;
        int    i,l,x,y;
        bool   sFirstLineBlank ;

        int    sRowCnt,sColumnCnt;
        char   init;

        char   cake[26][26];

	sFileIn  = fopen( "A-large.in", "r");
	sFileOut = fopen( "A-large.out.txt", "w+");

	fscanf( sFileIn, "%d\n", &sDataCnt );

        printf("%d\n",sDataCnt);

        for( i = 1 ; i <= sDataCnt ; i++ )
	{
            fscanf( sFileIn, "%d %d\n", &sRowCnt, &sColumnCnt );

            memset(cake, 0, 26*26);
            sFirstLineBlank = true;

            for( y = 0 ; y < sRowCnt ; y++)
            {
                fscanf( sFileIn, "%s\n", cake[y] );
            }

            for( y = 0 ; y < sRowCnt ; y++)
            {
                printf("%s\n",cake[y]);
                init = 0;
                for( x = 0 ; x < sColumnCnt ; x++ )
                {
                     if(cake[y][x] == '?' )
                     {
                         if( init != 0 )
                         {
                             cake[y][x] = init;
                         }
                         else{
                             continue;
                         }
                     }
                     else
                     {
                         if( init != 0 )
                         {
                             init = cake[y][x];
                         }
                         else
                         {
                             init = cake[y][x];
                             // 앞에 없다가 만든 경우
                             for(l = 0 ; l<x ; l++)
                             {
                                 cake[y][l] = init;
                             }
                         }
                     }
                 }

                 if((sFirstLineBlank == true) && (init != 0) && (y > 0 ))
                 {
                     //XS위로 체워 넣는다.
                     for( l = 0 ; l < y ; l++ )
                     {
                          memcpy(cake[l],cake[y],sColumnCnt);
                     }
                 }

                 if((sFirstLineBlank == false) && (init == 0) && ( y > 0 ))
                 {
                     memcpy(cake[y],cake[y-1],sColumnCnt);
                 }

                 if(init != 0)  sFirstLineBlank = false;
            }

            fprintf(sFileOut,"Case #%d:\n",i);
            for( y = 0 ; y < sRowCnt ; y++)
            {
                fprintf(sFileOut,"%s\n",cake[y]);
            }

        }
	fclose(sFileIn);
	fclose(sFileOut);

	return 0;
}
