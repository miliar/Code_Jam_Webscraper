#ifndef __OVERSIZED_PANCAKES_H__
#define __OVERSIZED_PANCAKES_H__

#include <vector>
#include <map>

struct pancakeset {
    std::vector<bool> pancakes;
    long flippersize;

    bool operator ==(const pancakeset& other) const {
        return pancakes == other.pancakes && flippersize == other.flippersize;
    }

    bool operator <(const pancakeset& other) const {
        return pancakes < other.pancakes;
    }
};

bool allhappy(std::vector<bool> pancakes);
long howmanymoves(pancakeset& set);
void howmanymoves_impl(pancakeset& current_set, std::map<pancakeset, long>&, std::recursive_mutex& used_sets_mutex, long& result, std::recursive_mutex& result_mutex, long depth);
std::vector<pancakeset> possible_mutations(pancakeset& set);

#endif // __OVERSIZED_PANCAKES_H__
