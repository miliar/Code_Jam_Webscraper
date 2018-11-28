#include <iostream>
#include <vector>

int main() {
    int num_instances;
    std::cin >> num_instances;
    for(size_t i = 0; i < num_instances; i++)
    {
        std::string inst_str;
        std::cin >> inst_str;
        int k;
        std::cin >> k;

        std::vector<bool> inst_bool;
        for(size_t ch = 0; ch < inst_str.length(); ch++)
        {
            inst_bool.push_back(inst_str[ch] == '+');
        }

        int count = 0;

        for(size_t j = 0; j + k - 1< inst_bool.size(); j++)
        {
            if(inst_bool[j] == false)
            {
                count++;
                for(size_t l = 0; l < k; l++)
                {
                    inst_bool[j+l] = not inst_bool[j+l];
                }
            }
        }

        std::string result;

        if(std::find(inst_bool.begin(),inst_bool.end(),false) == inst_bool.end())
        {
            result = std::to_string(count);
        } else{
            result = "IMPOSSIBLE";
        }

        std::cout << "Case #" << i + 1 << ": " << result << std::endl;
    }
    return 0;
}