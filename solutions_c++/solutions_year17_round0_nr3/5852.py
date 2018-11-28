#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <string>

const int length_size = 10;
std::map<std::string, int> lists[length_size];
char data[length_size] = {0};
int iteration = 0;
int cases = 1;
    FILE *out;
// To iterate, people take sets.
// To take seats, if odd left, subtract one, divide by two.
// If even left, divide by two and subtract one from a half.
// This will give ls, rs.

// If even, the person will take a seat on the left, meaning ls is smallest.

// Example, 36.  One person sits.  We now have 17, 18.
// Next, 18 sits, making the level 17.  Below, both now have 8,9's.
// Sit at 9's, then 8's.  Now, everything is 8's.
// 35.  One sits.  We now have 17, 17.
//Left, then right gives 16, 16.  Then down to all 8's.
void iterate(long long n, long long k)
{
    long long remain = k;
    int iteration = 0;
    // if even
    long long ls = n;
    long long rs = n;

    long long lscount = 0;
    long long rscount = 0;
    long long maximum;
    long long minimum;
    int symm = 0;
    int i;
    int result;

    beginning:;
    long long seated = 1<< iteration;
    if(seated >= remain)
    {

        if(rs == ls)
        {
            if(remain > rscount){
            printf("Hey1! %lld %lld %lld %lld %lld\n", rs, ls, seated, remain, rscount);

                if(ls % 2 == 0)
                {
                    rs = ls>> 1;
                    ls = rs-1;
                }
                else{
                    rs = ls = ls>> 1;
                }
            printf("Hey2! %lld %lld %lld %lld %lld\n", rs, ls, seated, remain, rscount);
            }
            else{
                //printf("abc %lld %lld, %lld %lld, %lld %lld \n", ls, rs,lscount, rscount, minimum, maximum);
                //printf("Hey2! %lld %lld %lld\n", seated, remain, rscount);
                if(rs % 2 == 0)
                {
                    rs = rs>> 1;
                    ls = rs-1;
                }
                else{
                        rs = ls = rs>> 1;
                }
            }
        }
        else{
            if(remain > rscount){
           // printf("Hey3! %lld %lld %lld\n", seated, remain, rscount);
                if(ls % 2 == 0)
                {
                    rs = ls>> 1;
                    ls = rs-1;
                }
                else{
                    rs = ls = ls>> 1;
                    rscount = (rscount << 1);
                }
            }
            else{
           // printf("Hey4! %lld %lld %lld\n", seated, remain, rscount);
                if(rs % 2 == 0)
                {
                    rs = rs>> 1;
                    ls = rs-1;
                }
                else{
                    rs = ls = rs>> 1;
                    rscount = (rscount << 1);
                }
            }
        }
            maximum = rs;
            minimum = ls;
        //printf("abc %lld %lld, %lld %lld, %lld %lld \n", ls, rs,lscount, rscount, minimum, maximum);
        goto done;
    }

    // The previous people takes a seat.
    remain -= seated;
    if(remain == 0){
        minimum = maximum = 0;
    }
    //The next people see these choices.

    if(rs == ls)
    {
        if(rs % 2 == 0)
        {
            printf("one45\n");
            rs = rs>> 1;
            ls = rs-1;
            lscount = rscount;
            if (iteration == 0){
                rscount = 1;
                lscount = 1;
            }

        }
        else{
       printf("oneasdf\n");
            rs = ls = rs>> 1;
            rscount = (rscount << 1);
             if (iteration == 0){
                rscount = 2;
            }
        }
    }
    else if(rs % 2 == 0)
    {
        //printf("one123\n");
        long long oldrs = rs;
        rs = rs>> 1;
        ls = rs-1;
        lscount = (lscount << 1) + rscount;
        rscount = rscount;
        if (iteration == 0){
            rscount = 1;
            lscount = 1;
        }
    }
    else{
        //printf("one234\n");
        rs = rs>> 1;
        ls = rs-1;
        rscount = (rscount << 1) + lscount;
        lscount = lscount;
        if(iteration == 0){
            rscount = 2;
        }
    }
    iteration++;
    //printf("%d: %lld %lld, count %lld %lld\n", iteration, ls, rs, lscount, rscount);
    goto beginning;
    done:;
    char buf[20];
    //fgets(buf, 20, stdin);
    printf("%lld %lld\n", maximum, minimum);
    fprintf(out,"Case #%d: %lld %lld\n", cases++, maximum, minimum);
}

int main()
{
    out = fopen("out.txt", "w");
    FILE *in = fopen("in.txt", "r");
    char buf[500];
    fgets(buf, 400, in);
    while(fgets(buf, 500, in))
    {
        while(buf[strlen(buf)-1] == '\n' || buf[strlen(buf)-1] == '\r')
            buf[strlen(buf)-1] = '\0';

        int i;
        long long n;
        long long k;
        sscanf(buf, "%lld %lld", &n, &k);
        iterate(n, k);


    }
    return 0;
}
