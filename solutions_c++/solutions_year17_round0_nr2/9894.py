//---------------------------------------------------------------------------
#include <iostream>
#include <fstream>
//#include <vcl>

using namespace std;
int main(int argc, char* argv[])
{
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        ifstream filei("B-large.in");
        ofstream fileo("answers.txt");
        char input[20];
        int c, a, n;
        filei>>c;
        a = c;
        while(c--)
        {
                n = 0;
                filei>>input;

                while(input[n] != '\0')
                        n++;
                for(int i = n-1; i > 0; i--)
                {
                        if(input[i] < input[i-1])
                        {
                                input[i-1]--;
                                for(int j = i; j < n; j++)
                                        input[j] = 57;
                        }
                }
                fileo<<"Case #"<<a-c<<": ";
                int i = 0;
                while(input[i] == '0')
                        i++;
                while(i < n)
                        fileo<<input[i++];
                fileo<<"\n";
        }
        filei.close();
        fileo.close();
        return 0;
}
