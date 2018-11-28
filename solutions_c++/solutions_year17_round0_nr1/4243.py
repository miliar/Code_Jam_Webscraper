#include <bits/stdc++.h>

using namespace std ;

int main()
{
    freopen("A-large.in", "r" , stdin);
    freopen("A_output.txt", "w" , stdout);
    int test_case , flipper;
    string config ;

    scanf("%d", &test_case);

    for(int k = 0 ; k < test_case ; k++)
    {
        cin >> config >> flipper ;

        int length = config.size();
        bool possible = true ;

        int counter = 0 ;
        for(int i = 0 ; i < length - flipper+1 ; i++)
        {
            //cout << config << endl ;
            if(config[i] == '-')
            {
                for(int j = i , iterate = 0 ; iterate < flipper ; iterate++ , j++)
                {
                    if(config[j] == '+')
                    {
                        config[j] = '-';
                    }
                    else if(config[j] == '-')
                    {
                        config[j] = '+';
                    }
                }
                counter++;
            }
        }

        for(int i = 0 ; i < length ; i++)
        {
            if(config[i] == '-')
            {
                possible = false ;
            }
        }
        if(possible)
        {
            printf("Case #%d: %d\n", k+1 , counter);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", k+1);
        }


    }


    return 0 ;
}
