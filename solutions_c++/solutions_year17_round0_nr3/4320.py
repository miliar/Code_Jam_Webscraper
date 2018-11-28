#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef unsigned long long ull;

int main() {
    int num_inputs;
    cin >> num_inputs;

    for (int i = 0; i < num_inputs; i++) {
        ull num_stalls;
        ull num_people;
        ull y;
        ull z;

        cin >> num_stalls >> num_people;

        // Decide the level of the binary tree
        // this person is in. And within that level,
        // decide this person's position.
        int level = log (1.0*num_people) / log (2.0);
        int position = num_people - pow (2, level);

        // Calculate list of elements in the binary tree
        // within that level. Level m should have 2^m elements;
        // and the sum of all elements in level m should be:
        // num_stalls-2^(m+1)+1
        vector<ull> element_list;
        unsigned int num_level_elements = pow (2, level);
        ull sum_elements = num_stalls - pow (2, level) + 1;
        ull smaller_element = sum_elements/num_level_elements;
        int num_larger_elements = sum_elements -
                            smaller_element * num_level_elements;
        int num_smaller_elements = num_level_elements - num_larger_elements;
        for (int j = 0; j < num_larger_elements; j++) {
            element_list.push_back(smaller_element + 1);
        }
        for (int j = 0; j < num_smaller_elements; j++) {
            element_list.push_back(smaller_element);
        }

        // Select the element for that person,
        // and compute y and z
        ull selected_element = element_list[position];
        if (selected_element%2) {
            y = z = (selected_element-1)/2;
        } else {
            y = selected_element/2;
            z = selected_element/2 - 1;
        }

        cout << "Case #" << i+1 << ": " << y << " " << z << endl;
    }
    return 0;
}
