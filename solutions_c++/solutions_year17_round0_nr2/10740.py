#include<cstdio>
#include<fstream>
//#include<iostream>



int main()
{
    int i, T, n, temp, x, y, count, done;

    freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );


    scanf("%d", &T);

    for (i=1; i<=T; i++){
        scanf("%d", &n);
        done = 0;
        while(done!=1){
            temp = n;
            count = 0;
            while(temp!=0){
               x = temp%10;
               y = (temp/10)%10;
               if (x<y){
                    count++;
                    //cout << x << " " << y << endl;
               }
               temp /= 10;
               //cout << temp << endl;
            }
            if (count>0) n--;
            else done = 1;
        }
        printf("Case #%d: %d\n", i, n);
    }
    return 0;
}
