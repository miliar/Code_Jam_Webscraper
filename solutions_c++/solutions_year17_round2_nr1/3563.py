#include <stdio.h>
#include <iomanip>

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>  // includes cin to read from stdin and cout to write to stdout


int main()
{
    double tc, D, N, K, S;
    char buff[1024];
    
    std::ifstream file("./a.txt");
    std::ofstream ofile("./o.txt");
    file >> tc;  // read t. cin knows that t is an int, so it reads it as such.

    
    for (int i = 1; i <= tc; ++i)
    {
        double max_time = 0;
        
        file >> D >> N;
        
        for (int n=0; n < N ; n++)
        {
            file >> K >> S;
            
            double time = (D-K)/S;
            if(time > max_time)
            {
                max_time = time;
            }
            //std::cout << D << ","<< K << ","<< S << ","<< max_time << "," << time << std::endl;
        }
        double AS = (double)D/max_time;
        sprintf(buff,"%.6f", AS);
        std::cout << "Case #" << i << ": "  << buff << std::endl;
        ofile << "Case #" << i << ": "      <<  buff << std::endl;
        
    }
    return 0;
}
