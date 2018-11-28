#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <time.h>

int main(int argc, char* argv[])
{
  int ncases = 0;
  std::cin >> ncases;
  std::ofstream out;
  out.open("result.txt");
  for(int kase = 0; kase < ncases; kase++)
  {
    std::string T = "";
    std::cin >> T;

    int noutput = -1;
    std::vector<int> input_value;
    for(int idx = 0; idx < T.length(); idx++)
    {
        int decimal = ((int) T[idx]) - 48;
        input_value.push_back(decimal);
    }

    int last_index = 0;
    // Forward pass
    for(int i = 0; i < (int) input_value.size(); i++)
    {
        if(i + 1 >= input_value.size())
        {
            last_index = i;
            break;
        }
        if(input_value[i] > input_value[i + 1])
        {
            last_index = i;
            break;
        }

    }
    if(last_index == (int) input_value.size() - 1)
    {
        out << "Case #" << (kase + 1) << ": " << T << std::endl;
        std::cout << "Case #" << (kase + 1) << ": " << T << " --> " << T << std::endl;
        continue;
    }
    else
    {
        // Backward pass
        input_value[last_index]--;
        while(last_index > 0)
        {
            if(input_value[last_index] < input_value[last_index - 1])
            {
                last_index--;
                input_value[last_index]--;
            }
            else
            {
                break;
            }
        }

        for(int i = last_index + 1; i < (int) input_value.size(); i++)
        {
            input_value[i] = 9;
        }


        out << "Case #" << (kase + 1) << ": ";
        std::cout << "Case #" << (kase + 1) << ": " << T << " --> ";

        unsigned long long int output_value = 0;
        for (int i = 0; i < (int) input_value.size(); i++)
        {
            int pow10 = (int) input_value.size() - 1 - i;
            unsigned long long int decimal_pow10 = (unsigned long long int) input_value[i];
            for(int p = 0; p < pow10; p++)
            {
                decimal_pow10 *= (unsigned long long int) 10;
            }
            output_value += decimal_pow10;
        }

        out << output_value;
        std::cout << output_value;
        out << std::endl;
        std::cout << std::endl;


    }
  }

  out.close();

  out.open("input.txt");
  ncases = 1000;
  out << ncases << std::endl;
  srand(time(NULL));
  for(int kase = 0; kase < ncases; kase++)
  {
      int value = rand() % 10000000;
      out << value << std::endl;
  }
  out.close();

  return 0;
}
