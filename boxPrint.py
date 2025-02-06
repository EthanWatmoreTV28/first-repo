sentence = """Understanding Gen Z Slang: The Rise of “Tuff”

Gen Z slang is ever-evolving, filled with playful and creative expressions that can sometimes be difficult to decode. One term that has recently gained popularity among this generation is “tuff.” While it may seem like a misspelling of “tough,” its meaning is anything but traditional. In Gen Z slang, “tuff” is used to describe something that is impressive, cool, or outstanding—think of it as a way to show admiration or recognition for something bold or unique.

Unlike the traditional use of “tough,” which implies strength or resilience, “tuff” carries a more laid-back, confident vibe. When something is described as “tuff,” it’s often because it stands out in an undeniable way, whether it’s an incredible accomplishment, a striking outfit, or even a person’s bold personality. It’s the kind of word that celebrates being unapologetically yourself and standing out from the crowd.

For example, if someone nails a challenging task or showcases an impressive skill, you might hear, “That was tuff!” It’s a compliment, suggesting that what the person did was not just good but exceptionally cool or noteworthy. Similarly, when someone is showing off their style or attitude in a way that feels daring or confident, they might be described as “tuff” for their boldness.

But “tuff” is not just a term of praise—it also reflects the Gen Z mindset, where being authentic and owning your individuality is celebrated. It’s less about conforming to traditional ideas of what’s “cool” and more about expressing yourself in ways that feel true to you.

In short, “tuff” has become a staple in Gen Z slang, embodying a spirit of confidence, creativity, and individuality. So, the next time you hear someone say “That’s tuff,” know that it’s not just about being tough—it’s about being undeniably cool."""

words = sentence.split()

longestString = max(words, key=len)

def maxStars(longestString):
    stars = (len(longestString)+4) * "*"
    print(stars)


maxStars(longestString)

for i in range(len(words)):
    difference = len(longestString) - len(words[i])
    space = int(difference/2 +1)
    
    print("*" + space * " "+ words[i] + space  * " " +"*")
    
maxStars(longestString)

